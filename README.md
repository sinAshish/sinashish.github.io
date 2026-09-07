# My Website

My academic website copied from [al-folio](https://alshedivat.github.io/al-folio/)

## Updating the Reading List

I maintain a custom, self-contained Reading List page directly integrated into my portfolio. Whenever you finish new books and want to update the website, follow these steps:

1. **Export your library:** Go to [Goodreads Import/Export](https://www.goodreads.com/review/import) and click **Export Library** to download your latest CSV library export.
2. **Save the CSV:** Save the downloaded CSV file into your local system's Downloads folder as:
   `~/Downloads/goodreads_library_export.csv`
3. **Run the update script:** Open your terminal in this repository's root directory and execute:
   ```bash
   python3 update_reading_from_csv.py
   ```

The script will automatically detect new books, download and optimize their cover thumbnails to `.webp` format in `assets/img/reading/` (using OpenLibrary, Google Books, and Bookshop.org fallbacks), group everything by year, and cleanly regenerate `_pages/reading.md`.
