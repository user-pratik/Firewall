import json
from detector import AnomalyDetector
from features import to_vector

def train_from_log(log_path="logs/traffic.log"):
    data = []
    with open(log_path) as f:
        for line in f:
            pkt = json.loads(line)
            vec = to_vector(pkt["features"])
            data.append(vec)

    model = AnomalyDetector()
    model.fit(data)

if __name__ == "__main__":
    train_from_log()

