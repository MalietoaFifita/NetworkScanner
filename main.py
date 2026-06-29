#subprocess module to run ping command
import subprocess
#socket module to run a hostname lookup
import socket
#time module to keep track of how long the scan takes
import time
#ANSI color codes for color output in terminal
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def main():
    #intro for user
    print("====Simple Network Scanner====")
    print("This program will scan a range of IP's")
    print("The IP's must be in the same network, with the starting IP smaller than the ending IP.")

    #while loop to keep scanning if user chooses
    while True:

        #starting time of the scan
        start_time = time.time()

        one_scan()

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


    

def one_scan():
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
        print(f"{YELLOW}Sorry, your IP's are not in the same network{RESET}")
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
    
    print("Scan Complete.")
    print(f"{GREEN}Hosts up: {hosts_up}{RESET}")
    print(f"{RED}Hosts down: {hosts_down}{RESET}")



def scan_ip(ip):
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



#if loop, makes it so that it will only execute this code if ran directly not if imported
if __name__ == "__main__":
    main()