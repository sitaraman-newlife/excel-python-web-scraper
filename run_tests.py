"""Comprehensive test runner for web scraper
Runs multiple test scenarios and provides detailed results
"""

from scraper import WebScraper
import os
import sys

print("\n" + "="*60)
print("   WEB SCRAPER - COMPREHENSIVE TEST SUITE")
print("="*60 + "\n")

test_results = []

def test_valid_website():
    """Test 1: Valid website with existing data"""
    print("[Test 1] Valid website with data...")
    try:
        scraper = WebScraper('https://quotes.toscrape.com/', 't1.xlsx')
        scraper.run(selector='span.text')
        
        if len(scraper.data) > 0 and os.path.exists('t1.xlsx'):
            print("  Result: PASS - Extracted", len(scraper.data), "items\n")
            return True
        else:
            print("  Result: FAIL - No data extracted\n")
            return False
    except Exception as e:
        print(f"  Result: ERROR - {e}\n")
        return False

def test_different_selector():
    """Test 2: Different CSS selector"""
    print("[Test 2] Different CSS selector (authors)...")
    try:
        scraper = WebScraper('https://quotes.toscrape.com/', 't2.xlsx')
        scraper.run(selector='small.author')
        
        if len(scraper.data) > 0:
            print("  Result: PASS - Extracted", len(scraper.data), "authors\n")
            return True
        else:
            print("  Result: FAIL - No authors extracted\n")
            return False
    except Exception as e:
        print(f"  Result: ERROR - {e}\n")
        return False

def test_invalid_selector():
    """Test 3: Invalid selector (should handle gracefully)"""
    print("[Test 3] Invalid CSS selector...")
    try:
        scraper = WebScraper('https://quotes.toscrape.com/', 't3.xlsx')
        scraper.run(selector='.nonexistent-class-xyz')
        
        # Should handle gracefully, not crash
        if len(scraper.data) == 0:
            print("  Result: PASS - Handled gracefully (no data)\n")
            return True
        else:
            print("  Result: UNEXPECTED - Found data with invalid selector\n")
            return False
    except Exception as e:
        print(f"  Result: ERROR - {e}\n")
        return False

def test_excel_file_creation():
    """Test 4: Check Excel file creation and format"""
    print("[Test 4] Excel file creation and format...")
    try:
        scraper = WebScraper('https://quotes.toscrape.com/', 't4.xlsx')
        scraper.data = [['Test 1'], ['Test 2'], ['Test 3']]
        result = scraper.export_to_excel()
        
        if result and os.path.exists('t4.xlsx'):
            file_size = os.path.getsize('t4.xlsx')
            print(f"  Result: PASS - File created ({file_size} bytes)\n")
            return True
        else:
            print("  Result: FAIL - File not created\n")
            return False
    except Exception as e:
        print(f"  Result: ERROR - {e}\n")
        return False

def test_log_file():
    """Test 5: Check logging functionality"""
    print("[Test 5] Logging functionality...")
    try:
        if os.path.exists('scraper.log'):
            with open('scraper.log', 'r') as f:
                lines = f.readlines()
            print(f"  Result: PASS - Log file exists ({len(lines)} lines)\n")
            return True
        else:
            print("  Result: FAIL - Log file not found\n")
            return False
    except Exception as e:
        print(f"  Result: ERROR - {e}\n")
        return False

# Run all tests
print("Starting tests...\n")

test_results.append(test_valid_website())
test_results.append(test_different_selector())
test_results.append(test_invalid_selector())
test_results.append(test_excel_file_creation())
test_results.append(test_log_file())

# Summary
passed = sum(test_results)
total = len(test_results)

print("="*60)
print("   TEST SUMMARY")
print("="*60)
print(f"\nTests Passed: {passed}/{total}")
print(f"Tests Failed: {total - passed}/{total}")
print(f"Success Rate: {(passed/total)*100:.1f}%\n")

if passed == total:
    print("All tests passed! Scraper is working correctly.")
else:
    print("Some tests failed. Check output above for details.")

print("\nGenerated files:")
for i in range(1, 5):
    filename = f't{i}.xlsx'
    if os.path.exists(filename):
        print(f"  - {filename}")

print("  - scraper.log\n")

# Cleanup
print("Cleaning up test files...")
for i in range(1, 5):
    filename = f't{i}.xlsx'
    if os.path.exists(filename):
        os.remove(filename)
        print(f"  Removed {filename}")

print("\nTest completed!\n")
