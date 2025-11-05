"""
Main Proof-of-Concept node for Sentinel-AI (C-MSADS)
Runs simulated sensor fusion and AI-based drone detection.
"""

import time
import random
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from config import *

class DroneDetector:
    def __init__(self):
        self.model = None
        self.scaler = None
        self._prepare_assets()

    def _prepare_assets(self):
        """Train or load model assets."""
        try:
            assets = joblib.load(MODEL_PATH)
            self.model = assets["classifier"]
            self.scaler = assets["scaler"]
            print("[INFO] Loaded existing model assets.")
        except Exception:
            print("[INFO] Training new lightweight model...")
            X_train = np.array([
                [0.9, 0.8, 1, 1],
                [0.2, 0.3, 0, 0],
                [0.7, 0.6, 1, 0],
                [0.3, 0.4, 0, 1]
            ])
            y_train = np.array([1, 0, 1, 0])
            self.scaler = StandardScaler().fit(X_train)
            X_scaled = self.scaler.transform(X_train)
            self.model = RandomForestClassifier().fit(X_scaled, y_train)
            joblib.dump({"classifier": self.model, "scaler": self.scaler}, MODEL_PATH)

    def detect(self, features):
        X_scaled = self.scaler.transform([features])
        prediction = self.model.predict(X_scaled)[0]
        return "Drone Detected" if prediction == 1 else "Clear Sky"


def get_simulated_sensor_data():
    """Return fake readings for [radar, rf, optical, ir]."""
    radar = round(random.uniform(0, 1), 2)
    rf = round(random.uniform(0, 1), 2)
    optical = random.choice([0, 1])
    ir = random.choice([0, 1])
    return [radar, rf, optical, ir]


if __name__ == "__main__":
    print("\n=== Sentinel-AI C-MSADS Simulation Start ===\n")
    detector = DroneDetector()

    for _ in range(10):  # run 10 detection cycles
        features = get_simulated_sensor_data()
        result = detector.detect(features)
        print(f"[{time.strftime('%H:%M:%S')}] {features} -> {result}")
        time.sleep(DETECTION_INTERVAL_SEC)

    print("\n[INFO] Simulation complete. Check logs in /data.\n")
