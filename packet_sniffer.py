from scapy.all import *
from google.cloud import firestore
import threading

db = firestore.Client()

def packet_callback(packet):
    packet_dict = {
        "timestamp": datetime.now().isoformat(),
        "summary": packet.summary()
    }

    if IP in packet:
        packet_dict["src"] = packet[IP].src
        packet_dict["dst"] = packet[IP].dst
        packet_dict["proto"] = packet[IP].proto

        if TCP in packet:
            packet_dict["sport"] = packet[TCP].sport
            packet_dict["dport"] = packet[TCP].dport
        elif UDP in packet:
            packet_dict["sport"] = packet[UDP].sport
            packet_dict["dport"] = packet[UDP].dport

        if DNS in packet:
            packet_dict["dns_query"] = packet[DNS].qd.qname.decode()

    print(f"Captured: {packet_dict}")
    db.collection('packets').add(packet_dict)

def sniff_rebex():
    sniff(filter="host test.rebex.net", prn=packet_callback, store=0)

def sniff_dns():
    sniff(filter="udp port 53", prn=packet_callback, store=0)

def sniff_jsonplaceholder():
    sniff(filter="host jsonplaceholder.typicode.com", prn=packet_callback, store=0)

if __name__ == "__main__":
    threads = [
        threading.Thread(target=sniff_rebex),
        threading.Thread(target=sniff_dns),
        threading.Thread(target=sniff_jsonplaceholder)
    ]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()