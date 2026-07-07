# YSec Toolkit

YSec Toolkit is a small command-line collection for DNS lookups, port scanning, banner grabbing, and HTTP header inspection.

## Features

- DNS resolution and subdomain enumeration
- Port scanning over a range of ports
- Banner grabbing for open services
- HTTP header retrieval for web targets
- Automatic JSON report generation in the reports folder

## Project structure

- main.py — interactive menu
- dns_lookup.py — DNS helper functions
- scanner.py — port scanning and reporting
- banner.py — banner grabbing helper
- http_header.py — HTTP response header helper
- reports/ — generated scan reports

## Usage

Run the toolkit:

```bash
python main.py
```

From the menu, choose:

1. DNS Lookup
2. Port Scan
3. Banner Grab
4. HTTP Headers
5. Exit

## Report output

Each port scan creates a JSON report in the reports directory, for example:

- reports/google.com.json
- reports/scanme.nmap.org.json
- reports/192.168.1.15.json

## Notes

This project is intended for educational use and should only be used on systems you own or are authorized to test.
