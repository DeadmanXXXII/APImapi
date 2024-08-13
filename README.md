# APImapi
API mapper

1. **Command-Line Interface (CLI) Integration**: Use the `argparse` library to handle CLI arguments.
2. **Recursive Crawling**: Continue to recursively crawl API endpoints.
3. **Output Handling**: Save results and provides user feedback through CLI.


### Summary of Features:

1. **Command-Line Arguments**:
   - `--url`: The base URL to start crawling from.
   - `--timesec`: The delay between requests (default is 0.5 seconds).
   - `--depth`: The maximum depth for crawling (default is 3).
   - `--output`: The file to save the results (default is `scraped_data.json`).

2. **Recursive Crawling**: The script recursively explores routes up to a specified depth.

3. **Error Handling**: Handles JSON parsing errors and HTTP request failures.

4. **Output**: Saves the collected data in a JSON file and prints a confirmation message.

### Running the Script

To run this script, you would use a command like:

```bash
pip install -r requirements.txt
```

```bash
python3 apimapi.py --url https://techcrunch.com/wp-json/tc/v1/ --timesec 1 --depth 3 --output api_map.json
```

![Example use amd output](https://github.com/DeadmanXXXII/APImapi/raw/main/Screenshot_20240813-205512.png)

