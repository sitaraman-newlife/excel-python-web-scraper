"""Basic test script for web scraper
Tests the scraper with a simple, reliable test website
"""

from scraper import WebScraper
import os

print("="*50)
print("TESTING WEB SCRAPER")
print("="*50)

# Test 1: Basic scraping test
print("\nTest 1: Scraping quotes from test website...")

scraper = WebScraper(
    url='https://quotes.toscrape.com/',
    output_file='test_output.xlsx'
)

print("Starting scraper...")
scraper.run(selector='span.text')

# Check results
if scraper.data:
    print(f"\n✓ SUCCESS: Extracted {len(scraper.data)} quotes")
    print(f"  Sample quote: {scraper.data[0][0][:50]}...")
else:
    print("\n✗ FAILED: No data extracted")

# Check if files were created
if os.path.exists('test_output.xlsx'):
    print("✓ Excel file created successfully")
    file_size = os.path.getsize('test_output.xlsx')
    print(f"  File size: {file_size} bytes")
else:
    print("✗ Excel file not created")

if os.path.exists('scraper.log'):
    print("✓ Log file created successfully")
else:
    print("✗ Log file not created")

print("\n" + "="*50)
print("TEST COMPLETED")
print("="*50)
print("\nCheck the following files:")
print("  - test_output.xlsx (scraped data)")
print("  - scraper.log (execution logs)")
print("\nTo run this test:")
print("  python test_scraper.py")
