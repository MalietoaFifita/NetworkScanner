import subprocess

def main():
    print("====Simple Network Scanner====")
    print("This program will scan a range of IP's")
    #variables to hold the ip's that we will be scanning
    start_ip = input("Enter the start ip: ")
        
    # validation check
    if not valid_ip(start_ip):
        print("That is not a valid ip")
        return

    end_ip = input("Enter the ending ip: ")

    #validation check
    if not valid_ip(end_ip):
        print("That is not a valid ip")
        return
    
    #split the ip's into 4 parts and extract the last number for the range values
    start_parts = start_ip.split(".")
    end_parts = end_ip.split(".")

    #extract the base of the ip's, should be the same for both
    base = ".".join(start_parts[:3]) + "."
    
    #get starting and ending integers of the range of ips
    start_range = int(start_parts[3])
    end_range = int(end_parts[3])

    for i in range(start_range, end_range + 1):
        ip = base + str(i)
        scan_ip(ip)


def scan_ip(ip):
    print(f"Scanning {ip}")
    #Scanning logic
    command = ["ping", "-n", "1", ip ]
    result = subprocess.run(command, capture_output=True , text=True)
    
    #if result return code = 0, then success if not then failure
    if result.returncode == 0:
        print(f"Host {ip} is up")
    else:
        print(f"Host {ip} is down")

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