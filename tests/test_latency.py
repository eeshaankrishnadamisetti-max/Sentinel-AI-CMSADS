import time
from sentinel_poc_node import DroneDetector, get_simulated_sensor_data

def test_latency():
    detector = DroneDetector()
    start = time.time()
    result = detector.detect(get_simulated_sensor_data())
    duration = time.time() - start
    print(f"Latency: {duration:.3f}s | Result: {result}")
    assert duration < 2.0
