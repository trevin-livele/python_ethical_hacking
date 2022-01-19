import scapy.all as scapy

def scanner(ip):
    scapy.arping(ip)
	print(request.summary()) #arp request
    request.show()


	broadcast = scapy.Ether()
	broadcast.dst = "ff:ff:ff:ff:ff" #broadcast mac
    broadcast.show()

	request_brodcast = broadcast/request
    request_brodcast.show()

scanner("192.168.1.1/24")
