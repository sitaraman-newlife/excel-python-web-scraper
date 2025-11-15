"""Configuration Example for Web Scraper
Copy this file to config.py and update with your settings.
"""

# Target website configuration
TARGET_URLS = [
    'https://example.com/page1',
    'https://example.com/page2',
    # Add more URLs as needed
]

# CSS Selectors for data extraction
SELECTORS = {
    'main_content': '.content-wrapper',
    'title': 'h1.title',
    'description': 'p.description',
    'price': 'span.price',
    # Add more selectors as needed
}

# Excel output configuration
OUTPUT_FILE = 'scraped_data.xlsx'
WORKSHEET_NAME = 'Data'

# Request configuration
REQUEST_TIMEOUT = 10  # seconds
REQUEST_DELAY = 1  # seconds between requests
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# Logging configuration
LOG_FILE = 'scraper.log'
LOG_LEVEL = 'INFO'  # Options: DEBUG, INFO, WARNING, ERROR

# Data validation
MIN_DATA_LENGTH = 1  # Minimum characters for valid data
REQUIRED_FIELDS = ['title']  # Fields that must be present

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
