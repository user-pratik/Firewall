from sklearn.ensemble import IsolationForest
import numpy as np
import os
import pickle

MODEL_PATH = "core/ml_agent/model.pkl"

class OnlineAnomalyDetector:
    def __init__(self):
        self.model = None
        if os.path.exists(MODEL_PATH):
            self.load_model()
        else:
            self.model = IsolationForest(contamination=0.05, n_estimators=100)
            # Cold start with some dummy samples to avoid crashes
            self.model.fit(np.random.rand(10, 4))

    def predict(self, features):
        X = np.array([features])
        return self.model.predict(X)[0] == -1

    def anomaly_score(self, features):
        X = np.array([features])
        return -self.model.decision_function(X)[0]  # Higher = more anomalous

    def load_model(self):
        with open(MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)

    def save_model(self):
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(self.model, f)

    def partial_fit(self, X):
        # Placeholder: scikit-learn IsolationForest doesn't support partial_fit
        # You could retrain or switch to online model like river or sklearn.pipeline with buffer
        pass

