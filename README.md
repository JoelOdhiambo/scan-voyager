# Scan Voyager

Scan Voyager is a simple Python script for port scanning. It allows you to scan a target IP address for open ports within a specified range.

## Features

- Scans a range of ports on a specified target IP address.
- Uses threading for concurrent scanning, improving performance.
- Displays open ports found during the scan.

## Getting Started

### Prerequisites

- Python 3.x
- `socket` library
- `concurrent.futures` library

### Usage

1. Clone the repository:

```bash
git clone https://github.com/JoelOdhiambo/scan-voyager.git
```

2. Navigate to the project directory:

```bash
cd scan-voyager
```

3. Run the script with Python, providing the target IP address as a command-line argument:

```bash
python3 scan-voyager.py <ip_address>
```
