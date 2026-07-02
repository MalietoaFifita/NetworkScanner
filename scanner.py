"""
Core scanning logic for the Simple Network Scanner.

This module contains:
- one_scan(): orchestrates a full scan of a user-defined IP range
- scan_ip(): performs a single host scan using ping and reverse DNS lookup

It relies on:
- subprocess for executing ping commands
- socket for hostname resolution
- utils.py for IP validation and ANSI color formatting

The functions here focus solely on scanning behavior and output formatting.
"""

#subprocess module to run ping command
import subprocess

#socket module to run a hostname lookup
import socket

#import valid ip and ANSI escape colors from utils since it calls it
from utils import valid_ip, GREEN, RED, YELLOW, RESET

def scan_range():
    """
    Performs a full scan across a user-defined IP range.

    Steps:
    - Prompt the user for a starting and ending IP address, validating both
    - Ensure both IPs belong to the same /24 network (first three octets match)
    - Ensure the starting IP's last octet is less than or equal to the ending IP's
    - Construct the base network prefix from the first three octets
    - Loop through the range of host addresses and scan each using scan_ip()
    - Print a summary showing how many hosts were up or down

    This function handles all validation and iteration logic for a single scan.
    """
    #Loop to keep trying to validate the IP
    while True:
        #variables to hold the ip's that we will be scanning
        start_ip = input("Enter the start ip: ")
        # validation check
        if valid_ip(start_ip):
            break
        print(f"{YELLOW}That is not a valid ip{RESET}")

    #Same loop to keep trying to validate the IP
    while True:
        end_ip = input("Enter the ending ip: ")
        #validation check
        if valid_ip(end_ip):
            break
        print(f"{YELLOW}That is not a valid ip{RESET}")
    
    #split the ip's into 4 parts and extract the last number for the range values
    start_parts = start_ip.split(".")
    end_parts = end_ip.split(".")

    #validation check to make sure ip's are in the same network
    if start_parts[:3] != end_parts[:3]:
        print(f"{YELLOW}Invalid range: both IPs must be in the same /24 network (first three octets must match).{RESET}")
        return
    
    #validation check to make sure last octets are in order, need to convert to int in order to compare
    if int(start_parts[3]) > int(end_parts[3]):
        print(f"{YELLOW}Sorry that is not a valid IP range{RESET}")
        return

    #put together the base of the ip's, should be the same for both
    base = ".".join(start_parts[:3]) + "."
    
    #get starting and ending integers of the range of ips
    start_range = int(start_parts[3])
    end_range = int(end_parts[3])

    #hosts variables to use in output
    hosts_up = 0
    hosts_down = 0

    #for range loop to loop through the range of IP's
    for i in range(start_range, end_range + 1):
        ip = base + str(i)
        if scan_ip(ip):
            #add 1 to hosts_up if it is up
            hosts_up += 1
        else:
            #add 1 to hosts_down if it is down
            hosts_down += 1
    
    print("================================")
    print("||         SCAN COMPLETE      ||")
    print("================================")
    print(f"{GREEN}Hosts up: {hosts_up}{RESET}")
    print(f"{RED}Hosts down: {hosts_down}{RESET}")



def scan_ip(ip):
    """
    Scans a single IP address using the system ping command.

    Steps:
    - Build a ping command that sends one packet for efficiency
    - Execute the command using subprocess and capture the output
    - If the ping succeeds, attempt reverse DNS lookup for a hostname
    - Print a formatted message indicating whether the host is up or down

    Returns:
    - True if the host responds to ping
    - False if the host is unreachable

    """

    #Scanning logic
    command = ["ping", "-n", "1", ip ]
    result = subprocess.run(command, capture_output=True , text=True)
    
    #if result return code = 0, means success so return true. if not, then return failure.
    if result.returncode == 0:
        try:
            #look for a hostname
            host_name = socket.gethostbyaddr(ip)[0]
        except:
            host_name = "Unknown"

        print(f"{GREEN}[+] {ip} ({host_name}) is up{RESET}")
        return True
    else:
        print(f"{RED}[-] {ip} is down{RESET}")
        return False
