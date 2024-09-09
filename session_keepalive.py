import requests
import time
import argparse
import sys
import logging

def parse_request_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables to store request components
    method, url, headers, body = '', '', {}, None
    
    # Parse the request from the file
    for i, line in enumerate(lines):
        line = line.strip()

        if i == 0:  # First line contains the method and the URL
            parts = line.split(' ', 2)
            if len(parts) == 3:
                method = parts[0]
                url = parts[1]
        elif line.lower().startswith('host:'):
            host = line.split(':', 1)[1].strip()
            url = f"https://{host}{url}"
        elif ': ' in line:  # Parse headers
            key, value = line.split(': ', 1)
            headers[key] = value
        elif line == '':  # Empty line indicates the body is about to start
            body = ''.join(lines[i + 1:]).strip()
            break

    return {
        'method': method.upper(),
        'url': url,
        'headers': headers,
        'data': body
    }

def send_web_request(request_details, proxies=None):
    method = request_details['method']
    url = request_details['url']
    headers = request_details['headers']
    data = request_details['data']

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, proxies=proxies)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=data, proxies=proxies)
        else:
            print(f"Unsupported HTTP method: {method}")
            return None

        # Log request and response details
        logging.info(f"Request sent: {method} {url}")
        logging.info(f"Headers: {headers}")
        if data:
            logging.info(f"Data: {data}")
        logging.info(f"Response status: {response.status_code}")
        logging.info(f"Response body: {response.text}")
        return response.status_code
    except Exception as e:
        logging.error(f"Failed to send request: {e}")
        return None

def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description="Send web requests to keep session active.")
    parser.add_argument('request_file', help="Path to the file containing the web request details.")
    parser.add_argument('interval', type=int, help="Time interval in seconds between requests.")
    parser.add_argument('--proxy', help="Proxy to use for the requests (e.g., http://proxy.example.com:8080).", default=None)
    
    args = parser.parse_args()

    # Parse the request file
    try:
        request_details = parse_request_file(args.request_file)
        if not request_details['method'] or not request_details['url']:
            logging.error("Invalid request file format.")
            sys.exit(1)
    except FileNotFoundError:
        logging.error(f"File not found: {args.request_file}")
        sys.exit(1)

    # Configure proxy if provided
    proxies = None
    if args.proxy:
        proxies = {
            'http': args.proxy,
            'https': args.proxy
        }
        logging.info(f"Using proxy: {args.proxy}")

    # Send web requests in a loop at the specified interval
    try:
        while True:
            send_web_request(request_details, proxies=proxies)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")

if __name__ == '__main__':
    main()
