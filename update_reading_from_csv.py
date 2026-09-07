import csv
import urllib.request
import json
import re
import os
import subprocess
from collections import defaultdict
import datetime
import ssl
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

# Group by year
grouped_books = defaultdict(list)
for b in books:
    grouped_books[b['year']].append(b)

sorted_years = sorted([y for y in grouped_books.keys() if y != "Unknown"], reverse=True)
if "Unknown" in grouped_books:
    sorted_years.append("Unknown")

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

print("Generating reading.md...")
html = """---
layout: page
title: reading list
permalink: /reading/
description: ""
nav: true
nav_order: 1
---

<div class="row align-items-center mb-4">
  <div class="col">
    <p class="mb-0" style="font-size: 1.1rem; line-height: 1.5;">
      Apart from research, I enjoy reading books and manga. I alternate between reading fiction and non-fiction books. Some of the books that I've read over the years are listed below. You can also see them on my <a href="https://goodreads.com/sinashish" target="_blank" rel="noopener noreferrer">Goodreads</a>. The books I especially liked are rated 4 or above.<br><span class="text-muted" style="font-size: 0.95rem;">Inspired by <a href="https://irenechen.net/reading-list/" target="_blank" rel="noopener noreferrer">Irene Chen's</a> page.</span>
    </p>
  </div>
  <div class="col-auto">
    <button class="btn btn-sm btn-outline-primary" id="toggle-view-btn" onclick="toggleView()" style="border-radius: 4px; font-weight: 500;">
      <i class="fa-solid fa-list mr-1"></i> List View
    </button>
  </div>
</div>

<div class="reading-list">
"""

for year in sorted_years:
    html += f"""
  <!-- {year} Section -->
  <div class="year-section mb-5">
    <h3 class="border-bottom pb-2 mb-4">{year}</h3>
    
    <!-- Grid View -->
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-6 g-4 grid-view-container">
"""
    for book in grouped_books[year]:
        basename = book['book_id']
        webp_path = f"assets/img/reading/{basename}.webp"
        
        has_cover = os.path.exists(webp_path)
        
        gr_url = f"https://www.goodreads.com/book/show/{book['book_id']}"
        
        stars_html = ""
        if book['rating'] > 0:
            stars_html = f"{book['rating']} ★"
            
        if has_cover:
            img_html = f'<img src="/assets/img/reading/{basename}.webp" class="card-img-top p-2" alt="{book["title"]}" style="object-fit: cover; height: 180px;">'
        else:
            # Fallback with book emoji beautifully styled
            img_html = f"""
            <div class="card-img-top p-2 d-flex align-items-center justify-content-center bg-light text-center" style="height: 180px;">
              <span style="font-size: 3rem; filter: grayscale(20%);">📖</span>
            </div>
            """
            
        html += f"""
      <div class="col mb-4">
        <div class="card h-100 hoverable">
          <a href="{gr_url}" target="_blank" rel="noopener noreferrer" class="text-reset d-block text-decoration-none h-100">
            {img_html}
            <div class="card-body p-2 d-flex flex-column" style="height: calc(100% - 180px);">
              <h5 class="card-title text-reset text-decoration-none" style="font-size: 0.9rem; margin-bottom: 0.25rem;">
                {book['title']}
              </h5>
              <div class="d-flex justify-content-between align-items-end mt-auto">
                <p class="card-text text-muted small mb-0">{book['author']}</p>
                <div class="text-muted small" style="font-size: 0.8rem;">
                  {stars_html}
                </div>
              </div>
            </div>
          </a>
        </div>
      </div>
"""
    html += f"""    </div>

    <!-- List View -->
    <div class="list-view-container d-none">
      <ul class="list-group" style="background: transparent;">
"""
    for idx, book in enumerate(grouped_books[year], 1):
        gr_url = f"https://www.goodreads.com/book/show/{book['book_id']}"
        stars_list_html = ""
        if book['rating'] > 0:
            stars_list_html = f"""<span class="text-muted small ml-2" style="font-size: 0.8rem;">{book['rating']} ★</span>"""
            
        html += f"""
        <li class="list-group-item d-flex justify-content-between align-items-center border-0 p-1 bg-transparent" style="font-size: 0.95rem;">
          <div class="ms-2 me-auto">
            <span class="text-muted mr-2 font-weight-bold" style="min-width: 25px; display: inline-block;">{idx}.</span>
            <a href="{gr_url}" target="_blank" rel="noopener noreferrer" class="text-reset font-weight-normal text-decoration-none">{book['title']}</a>
            <span class="text-muted small ml-1">by {book['author']}</span>
            {stars_list_html}
          </div>
        </li>
"""
    html += """      </ul>
    </div>

  </div>
"""

html += """</div>

<script>
function toggleView() {
  const btn = document.getElementById('toggle-view-btn');
  const grids = document.querySelectorAll('.grid-view-container');
  const lists = document.querySelectorAll('.list-view-container');
  
  if (btn.innerHTML.includes('List View')) {
    btn.innerHTML = '<i class="fa-solid fa-grip mr-1"></i> Grid View';
    grids.forEach(el => el.classList.add('d-none'));
    lists.forEach(el => el.classList.remove('d-none'));
  } else {
    btn.innerHTML = '<i class="fa-solid fa-list mr-1"></i> List View';
    grids.forEach(el => el.classList.remove('d-none'));
    lists.forEach(el => el.classList.add('d-none'));
  }
}
</script>
"""

with open('_pages/reading.md', 'w') as f:
    f.write(html)
    
print("Finished reading.md generation!")