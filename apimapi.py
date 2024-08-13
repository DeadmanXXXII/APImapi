import requests
import json
import time
import argparse
from urllib.parse import urljoin, urlparse

def check_endpoint(url, delay):
    time.sleep(delay)
    try:
        response = requests.get(url)
        print(f"Checked URL {url}, status code: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, dict):
                    return url, data
                elif isinstance(data, list):
                    return url, {"list": data}
                else:
                    return url, {"unexpected_type": str(type(data))}
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON from {url}: {e}")
        else:
            print(f"Failed to retrieve URL {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"Error with URL {url}: {e}")
    return None, None

def crawl_and_collect(url, collected_data, base_url, max_depth, delay, current_depth=0):
    if current_depth > max_depth:
        return

    url, data = check_endpoint(url, delay)
    if data:
        if isinstance(data, dict):
            routes = data.get("routes", {})
            for route, route_info in routes.items():
                full_url = urljoin(base_url, route)
                if full_url not in collected_data:
                    collected_data[full_url] = route_info
                    print(f"Discovered new route: {full_url}")
                    crawl_and_collect(full_url, collected_data, base_url, max_depth, delay, current_depth + 1)
        elif isinstance(data, dict) and "list" in data:
            collected_data[url] = data["list"]

def main():
    parser = argparse.ArgumentParser(description="APIMAPI: An API mapping and crawling tool")
    parser.add_argument('--url', required=True, help='Base URL of the API')
    parser.add_argument('--timesec', type=float, default=0.5, help='Delay between requests in seconds')
    parser.add_argument('--depth', type=int, default=3, help='Maximum depth of crawling')
    parser.add_argument('--output', default='api_map.json', help='Output file to save results')
    args = parser.parse_args()

    base_url = args.url
    delay = args.timesec
    max_depth = args.depth
    output_file = args.output

    collected_data = {}

    crawl_and_collect(base_url, collected_data, base_url, max_depth, delay)

    with open(output_file, 'w') as f:
        json.dump(collected_data, f, indent=4)

    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
