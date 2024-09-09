# Web Session Keep-Alive Tool

A powerful Python tool designed to help penetration testers and security professionals maintain active web sessions during testing. This tool allows users to send automated web requests at specified intervals, read request details from a file, and optionally use a proxy to route the requests. 

Created by **Sedric "Show Up Show Out" Louissaint**, this tool simplifies the process of keeping sessions active while performing security audits and penetration testing on web applications.

## Features
- **Automated Web Requests**: Send HTTP/HTTPS requests at a specified interval to maintain active sessions.
- **Customizable Request Input**: Parse HTTP request details from a text file, including headers, method, URL, and data.
- **Proxy Support**: Option to route web requests through a proxy (HTTP/HTTPS).
- **Verbose Logging**: Provides detailed logs of each request and response for transparency during testing.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Command-line Options](#command-line-options)
  - [Example Request File](#example-request-file)
- [Examples](#examples)
  - [Sending a GET Request](#sending-a-get-request)
  - [Sending a POST Request with Data](#sending-a-post-request-with-data)
  - [Using a Proxy](#using-a-proxy)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Installation
To install the tool, you’ll need Python 3.x and the `requests` library. You can install the required dependencies by running:

```bash
pip install requests
```

Alternatively, you can set up a virtual environment to avoid conflicts with global dependencies:

```bash
python3 -m venv env
source env/bin/activate
pip install requests
```

## Usage

The tool reads request details from a specified file, sends the requests at the desired interval, and optionally routes the requests through a proxy. 

### Command-line Options

```bash
python session_keepalive.py <request_file> <interval_in_seconds> [--proxy <proxy_url>]
```

- `request_file`: Path to the file containing the HTTP request details (required).
- `interval_in_seconds`: The time interval (in seconds) between each request (required).
- `--proxy`: The URL of the proxy to use (optional).

### Example Request File
Here’s an example of a properly formatted request file:

```
GET /api/keepalive?SessionId=12345678 HTTP/2
Host: testing.host.com
Accept-Language: en,en-gb;q=0.5
Accept-Charset: UTF-8;q=0.7,*;q=0.7
Pragma: no-cache
Cache-Control: no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0
Expires: Sat, 1 Jan 2000 00:00:00 GMT
Hmactype: SHA256
Securityversion: 1.1
User-Agent: Mozilla/5.0 (Linux; Android 13; SM-S134DL Build/TP1A.220624.014; wv)
Authorization: <your_auth_token>
Sentry-Trace: <trace_id>
...
```

### Examples

#### Sending a GET Request
To send a simple GET request at 60-second intervals:

```bash
python session_keepalive.py request.txt 60
```

#### Sending a POST Request with Data
If your request file includes data for a POST request, the tool will automatically include it in the body of the request.

```bash
python session_keepalive.py request_with_post.txt 30
```

#### Using a Proxy
To route the web requests through a proxy server, specify the proxy using the `--proxy` option:

```bash
python session_keepalive.py request.txt 60 --proxy http://proxy.example.com:8080
```

## Contributing
We welcome contributions from the community. To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

Feel free to open issues for bug reports, feature requests, or general feedback.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Credits
Created by **Sedric "Show Up Show Out" Louissaint**. Special thanks to everyone contributing to the security community and making web applications more secure through proper testing and automation.

### SEO Keywords (To improve visibility)
- Web Session Keep-Alive
- Python Web Automation
- Web Penetration Testing Tool
- Automated HTTP Requests
- Session Management Tool
- Web Security Testing
- Proxy Routing for Web Requests
- Web Application Security Tools
- HTTP/HTTPS Request Automation
- Session Timeout Prevention
- Python Network Tools for Security
