#SYN scanning
#UDP scanning
#Comprehensive


import nmap
scanner = nmap.portscanner()
print ("welcome to our nmap port scanner")

print ("<------------------------------------------------->")
ip addr = input("please enter the ip adress you want to scan")
print("the ip address is : " , ip_addr)
type(ip_addr)
resp = input("""\n please enter the type of scan you want to perform
                           1. SYN ACK scan
                           2. UDP scan
                           3. Comprehensive scan \n""")

print("You have selected option: " ,resp)


if resp == '1':
    print ("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_addr] .state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ",scanner[ip_addr]['tcp'].keys())
    #dict {][123,45,455]}

elif resp == '2':
    print ("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_addr] .state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ",scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print ("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sS -sV sC -A -O')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_addr] .state())#up
    print(scanner[ip_addr].all_protocols())#tcp
    print("open ports: ",scanner[ip_addr]['tcp'].keys())

elif resp >= 4:
    print("invalid please enter valid options")
