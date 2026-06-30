"""
Utility functions and shared constants for the Simple Network Scanner.

Includes:
- ANSI color codes for formatted terminal output
- valid_ip(): helper function to validate IPv4 address strings

This module provides reusable components that support both main.py
and scanner.py, keeping common logic centralized and easy to maintain.
"""

#ANSI color codes for color output in terminal
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def valid_ip(ip):
    parts = ip.split(".")

    #checks is ip is 4 parts, if not return false
    if len(parts) != 4:
        return False

    #checks if ip parts are all numbers, if not return false   
    for part in parts:
        if not part.isdigit():
            return False
    
        #convert each part to an int to see if they are valid number, if they aren't then return false
        digit = int(part)
        if digit < 0 or digit > 255:
            return False

    return True