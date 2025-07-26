def extract_features(log):
    try:
        return [
            int(log.get("proto", 0)),
            int(log.get("src_port") or -1),
            int(log.get("dst_port") or -1),
            int(log.get("length", 0))
        ]
    except Exception as e:
        print(f"[features] Error extracting: {e}")
        return None

