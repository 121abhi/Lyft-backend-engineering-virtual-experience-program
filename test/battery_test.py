import unittest
import datetime

from battery.battery_type.nubbin_battery import NubbinBattery
from battery.battery_type.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_ture(self):
        current_date = datetime.datetime(2022, 7, 31)
        last_service_date = datetime.datetime(2019, 1, 27)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.need_services())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2022, 7, 31)
        last_service_date = datetime.datetime(2021, 1, 10)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.need_services())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023, 6, 3)
        last_ser_date = datetime.datetime(2021, 5, 1)
        battery = SpindlerBattery(current_date, last_ser_date)
        self.assertTrue(battery.need_services())
    
    def test_needs_service_false(self):
        cur_date = datetime.datetime(2023, 6, 3)
        last_ser_date = datetime.datetime(2022, 6, 3)
        battery = SpindlerBattery(cur_date, last_ser_date)
        self.assertFalse(battery.need_services())
