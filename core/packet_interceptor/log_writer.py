# core/packet_interceptor/log_writer.py

import json
import os
from datetime import datetime

LOG_PATH = "logs/traffic.log"

def write_log(src, dst, proto, length, src_port=None, dst_port=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "src_ip": src,
        "dst_ip": dst,
        "proto": proto,
        "length": length,
        "src_port": src_port,
        "dst_port": dst_port
    }

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

