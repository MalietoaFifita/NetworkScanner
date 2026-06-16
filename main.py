import subprocess

def main():
    print("====Simple Network Scanner====")
    #variable to hold the ip that we will be scanning
    target = input("Enter the ip you would like to scan: ")
    scan_ip(target)

def scan_ip(ip):
    print(f"Scanning {ip}")
    #Scanning logic
    command = ["ping", "-n", "1", ip ]
    result = subprocess.run(command, capture_output=True , text=True)
    
    #if result return code = 0, then success if not then failure
    if result.returncode == 0:
        print(f"Host {ip} is up")
        #prints the output of the command
        print(result.stdout)
    else:
        print(f"Host {ip} is down")

#if loop, makes it so that it will only execute this code if ran directly not if imported
if __name__ == "__main__":
    main()