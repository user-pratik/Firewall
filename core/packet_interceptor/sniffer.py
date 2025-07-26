# core/packet_interceptor/sniffer.py

import sys
import os

# Ensure core/ is in sys.path for relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from scapy.all import sniff, IP, TCP, UDP
from core.packet_interceptor.log_writer import write_log

def extract_features(packet):
    if not packet.haslayer(IP):
        return None

    ip_layer = packet[IP]
    proto = packet.proto

    src_port = None
    dst_port = None

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
    elif UDP in packet:
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    return {
        "src_ip": ip_layer.src,
        "dst_ip": ip_layer.dst,
        "proto": proto,
        "src_port": src_port,
        "dst_port": dst_port,
        "len": len(packet)
    }

def process_packet(packet):
    data = extract_features(packet)
    if data:
        print(f"[sniffer] Packet: {data}")
        write_log(
            src=data["src_ip"],
            dst=data["dst_ip"],
            proto=data["proto"],
            length=data["len"]
        )

if __name__ == "__main__":
    interface = "enp0s3"  # replace with your interface name
    print(f"[sniffer] Listening on {interface} ...")
    sniff(iface=interface, prn=process_packet, store=0)

