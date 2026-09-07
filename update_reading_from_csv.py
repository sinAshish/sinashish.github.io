import csv
import urllib.request
import json
import re
import os
import subprocess
import datetime
import ssl
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

csv_file = "/Users/ashish.sinha/Downloads/goodreads_library_export.csv"
books = []

def get_cover_url(isbn, title, author):
    # Source 1: OpenLibrary by ISBN
    if isbn:
        ol_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg"
        try:
            req_img = urllib.request.Request(ol_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_img, context=ctx, timeout=3) as res:
                if int(res.headers.get('content-length', 1000)) > 100:
                    return ol_url
        except:
            pass
            
    # Source 2: Google Books API by ISBN
    if isbn:
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
                data = json.loads(res.read())
                if data.get('items'):
                    links = data['items'][0].get('volumeInfo', {}).get('imageLinks', {})
                    img = links.get('thumbnail') or links.get('smallThumbnail')
                    if img:
                        return img.replace('http://', 'https://')
        except:
            pass

    # Source 3: OpenLibrary Search API (by Title + Author)
    import urllib.parse
    query = urllib.parse.quote(f"{title} {author}")
    url = f"https://openlibrary.org/search.json?q={query}&limit=1"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
            data = json.loads(res.read())
            if data.get('docs') and data['docs'][0].get('cover_i'):
                return f"https://covers.openlibrary.org/b/id/{data['docs'][0]['cover_i']}-M.jpg"
    except:
        pass
        
    # Source 4: Google Books API (by Title + Author)
    try:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
            data = json.loads(res.read())
            if data.get('items'):
                links = data['items'][0].get('volumeInfo', {}).get('imageLinks', {})
                img = links.get('thumbnail') or links.get('smallThumbnail')
                if img:
                    return img.replace('http://', 'https://')
    except:
        pass
            
    return None

def clean_isbn(val):
    if not val: return ""
    return re.sub(r'[^0-9X]', '', val)

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        shelf = row.get('Exclusive Shelf', '').lower().strip()
        
        rating = 0
        try:
            rating = int(float(row.get('My Rating', 0)))
        except:
            pass
            
        # Filter read list
        if shelf != 'read':
            if shelf == 'did-not-finish' and rating > 0:
                pass
            else:
                continue
            
        title = row.get('Title', 'Unknown')
        author = row.get('Author', 'Unknown')
        
        # Clean title (parentheses & colons)
        original_title = title
        if '(' in title:
            title = title.split('(')[0].strip()
        if ':' in title:
            title = title.split(':')[0].strip()
            
        date_read = row.get('Date Read', '')
        date_added = row.get('Date Added', '')
        
        date_str = date_read if date_read else date_added
        year = "Unknown"
        if date_str:
            try:
                dt = datetime.datetime.strptime(date_str, "%Y/%m/%d")
                year = str(dt.year)
            except:
                pass
        
        # Berserk Deluxe 3 & 4 year check: Date read is actually empty in CSV, so we default to 2025 as requested
        if "Berserk Deluxe Edition" in original_title and ("Volume 3" in original_title or "Volume 4" in original_title):
            year = "2025"
            
        isbn13 = clean_isbn(row.get('ISBN13', ''))
        isbn10 = clean_isbn(row.get('ISBN', ''))
        isbn_to_use = isbn13 if isbn13 else isbn10
        book_id = row.get('Book Id')
        
        books.append({
            'title': title,
            'author': author,
            'rating': rating,
            'year': year,
            'isbn': isbn_to_use,
            'book_id': book_id
        })

os.makedirs('assets/img/reading', exist_ok=True)

# Parallel download helper
def download_and_convert_cover(book):
    isbn = book['isbn']
    basename = book['book_id']
    webp_path = f"assets/img/reading/{basename}.webp"
    
    if os.path.exists(webp_path):
        return webp_path
        
    img_url = get_cover_url(isbn, book['title'], book['author'])
    if img_url:
        try:
            req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
            img_data = urllib.request.urlopen(req_img, context=ctx, timeout=5).read()
            jpg_path = f"assets/img/reading/{basename}.jpg"
            with open(jpg_path, 'wb') as f:
                f.write(img_data)
            subprocess.run(["cwebp", "-q", "80", jpg_path, "-o", webp_path], capture_output=True)
            os.remove(jpg_path)
            return webp_path
        except:
            pass
    return None

print("Starting parallel cover downloads...")
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(download_and_convert_cover, b): b for b in books}
    for future in as_completed(futures):
        b = futures[future]
        res = future.result()

# Write to YAML data file
os.makedirs('_data', exist_ok=True)

# Create simplified structure for YAML
yaml_data = []
for book in books:
    basename = book['book_id']
    webp_path = f"assets/img/reading/{basename}.webp"
    has_cover = os.path.exists(webp_path)
    
    yaml_data.append({
        'book_id': book['book_id'],
        'title': book['title'],
        'author': book['author'],
        'rating': book['rating'],
        'year': book['year'],
        'has_cover': has_cover
    })

with open('_data/reading.yml', 'w', encoding='utf-8') as f:
    yaml.safe_dump(yaml_data, f, default_flow_style=False, allow_unicode=True)

print("Finished generating _data/reading.yml!")