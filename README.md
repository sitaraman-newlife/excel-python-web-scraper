# Excel & Python Web Scraper Automation

A professional Python-based web scraping tool that automatically extracts data from websites and exports it to Excel files with proper formatting and error handling.

## Features

- Web scraping using BeautifulSoup and Requests
- Automatic Excel export with openpyxl
- Comprehensive logging system
- Error handling and retry mechanisms
- Customizable CSS selectors
- Data validation and integrity checks
- Formatted Excel output with headers and metadata
- Support for multiple data sources

## Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

## Installation

1. Clone this repository:
```bash
git clone https://github.com/sitaraman-newlife/excel-python-web-scraper.git
cd excel-python-web-scraper
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from scraper import WebScraper

# Initialize the scraper
scraper = WebScraper(
    url='https://example.com/data-page',
    output_file='output.xlsx'
)

# Run scraper with CSS selector
scraper.run(selector='.data-item')
```

### Advanced Usage

```python
from scraper import WebScraper

# Create scraper instance
scraper = WebScraper('https://example.com', 'results.xlsx')

# Fetch and parse data
soup = scraper.fetch_page()
if soup:
    scraper.parse_data(soup, selector='.product-item')
    scraper.export_to_excel()
```

## Configuration

Update the following variables in `scraper.py`:

- `target_url`: The website URL to scrape
- `css_selector`: CSS selector for target elements
- `output_file`: Name of output Excel file

## File Structure

```
excel-python-web-scraper/
├── scraper.py          # Main scraping script
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore rules
└── scraper.log        # Generated log file
```

## Features in Detail

### Logging
All operations are logged to `scraper.log` with timestamps and severity levels.

### Excel Export
- Headers with bold formatting
- Auto-adjusted column widths
- Metadata (timestamp, source URL)
- Clean, professional output

### Error Handling
- Request timeouts
- HTTP error handling
- Parse error handling
- File I/O error handling

## Example Output

The script generates an Excel file with:
- Column A: Scraped content
- Column C-D: Metadata (timestamp, source URL)
- Formatted headers
- Professional styling

## Customization

To scrape different websites:

1. Update the `target_url` variable
2. Inspect the target website to find the correct CSS selector
3. Update the `css_selector` variable
4. Run the script

## Troubleshooting

- **No data extracted**: Check your CSS selector using browser dev tools
- **Connection errors**: Verify the URL and your internet connection
- **Permission errors**: Ensure write permissions for output directory

## Best Practices

- Always check the website's robots.txt and terms of service
- Implement rate limiting for large-scale scraping
- Use appropriate User-Agent headers
- Handle website changes and structure updates

## License

This project is available for educational and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Support

For issues or questions, please open an issue on GitHub.

## Author

Developed for the Freelancer Excel & Python Automation Specialist project.

## Changelog

### Version 1.0.0
- Initial release
- Basic web scraping functionality
- Excel export with formatting
- Logging system
- Error handling
