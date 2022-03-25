from random import randint


class Building:
    __floors_amount = randint(5, 20)
    floors = []

    def get_floors_amount(self):
        return self.__floors_amount


class Floor:
    def __init__(self, floor_number, floor_amount, passengers=[]):
        self.__amount_passengers = randint(0, 10)
        self.floor_number = floor_number
        self.floor_amount = floor_amount
        self.passengers = passengers

    def get_amount_passengers(self):
        return self.__amount_passengers

    def up(self):
        if self.floor_number != self.floor_amount:
            print('up')
        else:
            raise ValueError('нельзя подняться выше')

    def down(self):
        if self.floor_number != 1:
            print('down')
        else:
            raise ValueError('нельзя опуститься ниже')

    def __str__(self):
        return f'{self.floor_number}'


class Passenger:
    def __init__(self, current_floor, desired_floor):
        self.current_floor = current_floor
        self.desired_floor = desired_floor

    def __str__(self):
        return f'{self.desired_floor}'


class Elevator:
    __max_passengers = 5
    # if direction is True elevator goes up else elevator goes down
    __direction = True

    # passengers inside elevator
    __passengers = None

    # elevator goes to max_floor
    max_floor = None

    def __init__(self):
        self.position = 1

    def go(self):
        if self.__direction and self.position < self.max_floor:
            self.position += 1

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = direction

    def get_passengers(self):
        return self.__passengers

    def set_passengers(self, passengers):
        self.__passengers = passengers






