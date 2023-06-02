from car import Car

from battery.battery_type.nubbin_battery import NubbinBattery
from battery.battery_type.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car
        
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        enigne = SternmanEngine(last_service_date, warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car
        

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car