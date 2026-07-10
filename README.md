NETWORK SCANNER - Network Scanning Tool
Version 1.0 - July 2026

Network Scanner is a command line Python-based network scanning tool via IPv4 addresses. It scans for IP addresses, sanitizes user input, and times how long the scan takes. It also has the functionality to save the results of the scan to a text file.

Features:

- Scan any IPv4 range within the same /24 network  
- Input sanitization and validation  
- ANSI color-coded terminal output  
- Hostname lookup (reverse DNS)  
- Scan duration reporting  
- Summary of hosts up/down  
- Option to save results to `scan_results.txt`  
- Modular code structure (main, scanner, utils)

Why I Built This:
As an IT Support Specialist, I often need to quickly determine which devices on a network are online or responding to pings. This tool gives me a simple, fast way to scan a range of IPs and see which endpoints are reachable — something useful in real troubleshooting scenarios.

How to Run:
1. Install Python 3  
2. Download the project files:  
   - `main.py`  
   - `scanner.py`  
   - `utils.py`  
3. Place all files in the same directory  
4. Open a terminal and navigate to the project folder  
5. Run the tool: 
    - python main.py
    - Follow the on-screen instructions to enter your IP range and choose whether to save results.

Example Output:
================================
||       SCAN COMPLETE        ||
================================
Scan completed in 0.52 seconds
Hosts up: 1
Hosts down: 2

Example saved file:
Scan Results
========================
8.8.8.8 is up
8.8.8.9 is down
8.8.8.10 is down


Future Improvements:
- Multi-threaded scanning for faster performance  
- Cross-network scanning (beyond /24 ranges)  
- Port scanning capabilities  
- Optional verbose mode  
- Export results in JSON or CSV  

Author:
Malietoa  
IT Support Specialist & Aspiring Software Engineer
Denver, CO

