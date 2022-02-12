class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.max_num = {1: big, 2: medium, 3: small, }
        self.count = {1: 0, 2: 0, 3: 0, }

    def addCar(self, carType: int) -> bool:
        if self.count[carType] + 1 > self.max_num[carType]:
            return False
        self.count[carType] += 1
        return True
