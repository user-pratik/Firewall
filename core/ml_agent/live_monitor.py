import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from river import anomaly
from core.packet_interceptor.preprocessor import extract_features
from core.ml_agent.model_state import model

with open("logs/traffic.log", "r") as f:
    for line in f:
        data = json.loads(line.strip())
        features = extract_features(data)

        # Predict anomaly score
        score = model.score_one(features)

        if score > 0.75:
            print(f"[ALERT] Anomaly detected: {features} | Score: {score:.2f}")
            # Optional: block using firewall.manager

        # Train on the current data
        model = model.learn_one(features)

