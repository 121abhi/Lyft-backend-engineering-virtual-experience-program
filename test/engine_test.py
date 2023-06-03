from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

import unittest

class Test_Willoughby_Engine(unittest.TestCase):
    def test_needs_service_true(self):
        cur_mileage = 67031
        last_service_mileage = 0
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        cur_mileage = 55000
        last_service_mileage = 0
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class Test_Capulet_Engine(unittest.TestCase):
    def test_needs_service_true(self):
        cur_mileage = 31000
        last_service_mileage = 0 
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        cur_mileage = 27000
        last_service_mileage = 0 
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class Test_Sternman_Engine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())