from car_service.models import Position
from car_service.models import ServiceCenter
from car_service.models import Employee
from car_service.models import Client
from car_service.models import Car
from car_service.models import Part
from car_service.models import Service
from car_service.models import Repair
from car_service.models import RepairDetail

from car_service.repositories.BaseRepository import BaseRepository


class PositionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Position)


class ServiceCenterRepository(BaseRepository):
    def __init__(self):
        super().__init__(ServiceCenter)


class EmployeeRepository(BaseRepository):
    def __init__(self):
        super().__init__(Employee)


class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)


class CarRepository(BaseRepository):
    def __init__(self):
        super().__init__(Car)


class PartRepository(BaseRepository):
    def __init__(self):
        super().__init__(Part)


class ServiceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Service)


class RepairRepository(BaseRepository):
    def __init__(self):
        super().__init__(Repair)


class RepairDetailRepository(BaseRepository):
    def __init__(self):
        super().__init__(RepairDetail)
