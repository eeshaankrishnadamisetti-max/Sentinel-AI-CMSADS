import unittest
from sentinel_poc_node import get_simulated_sensor_data

class TestSensorSim(unittest.TestCase):
    def test_sensor_data_length(self):
        data = get_simulated_sensor_data()
        self.assertEqual(len(data), 4)

    def test_sensor_data_range(self):
        radar, rf, optical, ir = get_simulated_sensor_data()
        self.assertTrue(0 <= radar <= 1)
        self.assertTrue(0 <= rf <= 1)
        self.assertIn(optical, [0, 1])
        self.assertIn(ir, [0, 1])

if __name__ == "__main__":
    unittest.main()
