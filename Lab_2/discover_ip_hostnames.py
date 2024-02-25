import nmap

def map_subnet(subnet):
    output_filename = "subnet_mapping.txt"  # Fixed output file name
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-sn')

    with open(output_filename, 'w') as file:
        for host in nm.all_hosts():
            try:
                hostname = nm[host]['hostnames'][0]['name']
                file.write(f"IP: {host}\tHostname: {hostname}\n")
            except IndexError:
                file.write(f"IP: {host}\tHostname: Hostname not found\n")

if __name__ == "__main__":
    subnet = input("Enter the subnet (e.g., 192.168.1.0/24): ")
    map_subnet(subnet)