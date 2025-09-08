import unittest
from taxi_fare_app import calculate_taxi_fare

class TestTaxiFareCalculator(unittest.TestCase):

    def test_urban_taxi_short_distance(self):
        fare = calculate_taxi_fare("Urban", distance=1.5, waiting_time=0, baggage_count=0, animals=False, booking=False, toll=0)
        self.assertEqual(fare, 29.0)

    def test_urban_taxi_long_distance(self):
        fare = calculate_taxi_fare("Urban", distance=5, waiting_time=0, baggage_count=0, animals=False, booking=False, toll=0)
        self.assertAlmostEqual(fare, 60.5, places=1)

    def test_new_territories_taxi_with_waiting(self):
        fare = calculate_taxi_fare("New Territories", distance=3, waiting_time=10, baggage_count=0, animals=False, booking=False, toll=0)
        self.assertAlmostEqual(fare, 47.0, places=1)

    def test_lantau_taxi_with_extras(self):
        fare = calculate_taxi_fare("Lantau", distance=2, waiting_time=5, baggage_count=2, animals=True, booking=True, toll=20)
        self.assertAlmostEqual(fare, 72.0, places=1)

    def test_urban_taxi_high_fare_threshold(self):
        fare = calculate_taxi_fare("Urban", distance=20, waiting_time=0, baggage_count=0, animals=False, booking=False, toll=0)
        self.assertAlmostEqual(fare, 160.17, places=1)

if __name__ == "__main__":
    unittest.main()
