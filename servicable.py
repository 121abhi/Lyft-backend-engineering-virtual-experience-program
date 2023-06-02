from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def need_services(self):
        pass