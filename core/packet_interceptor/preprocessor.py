def extract_features(pkt):
    return {
        "src": pkt[0].src if hasattr(pkt[0], 'src') else None,
        "dst": pkt[0].dst if hasattr(pkt[0], 'dst') else None,
        "proto": pkt.proto if hasattr(pkt, 'proto') else "unknown",
        "length": len(pkt)
    }

