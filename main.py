"""
Main entry point for the Simple Network Scanner.

This module handles:
- User interaction and program flow
- Timing each scan operation
- Repeated scan prompts and validation
- Displaying high-level results to the user

All scanning logic is delegated to scanner.py, and shared utilities
(such as IP validation and ANSI color codes) are imported from utils.py.
"""

#time module to keep track of how long the scan takes
import time

#import functions from scanner.py file
from scanner import scan_range

#import functions and ANSI escape codes from utils.py
from utils import valid_ip, GREEN, RED, YELLOW, RESET

def main():
    """
    Runs the main program loop for the Simple Network Scanner.

    Responsibilities:
    - Display introductory information to the user
    - Record the start and end time of each scan to calculate duration
    - Call scan_range() to perform the actual network scan
    - Prompt the user to run another scan, validating input ('y' or 'n')

    This function controls overall program flow and user interaction.
    """
    #intro for user
    print("====Simple Network Scanner====")
    print("This program will scan a range of IP's")
    print("The IP's must be in the same network, with the starting IP smaller than the ending IP.")

    #while loop to keep scanning if user chooses
    while True:

        #starting time of the scan
        start_time = time.time()

        scan_range()

        #ending time of the scan
        end_time = time.time()

        duration = end_time - start_time
        print(f"{GREEN}Scan completed in {duration:.2f} seconds{RESET}")

        #Validation loop to ask user if they want to scan again
        while True:
            #ask user if they want to scan another range
            scan_again = input("Do you want to scan again? y/n: ").lower()

            if scan_again in ("y", "n"):
                break
            
            print(f"{YELLOW}Please enter 'y' or 'n'{RESET}")

        if scan_again == "n":
            break

#if loop, makes it so that it will only execute this code if ran directly not if imported
if __name__ == "__main__":
    main()