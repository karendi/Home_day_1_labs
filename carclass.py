class Car(object):
    def __init__(self, name = 'General', model = 'GM' , speed = 0):
        self.name = name
        self.model = model
        self.type_of_vehicle = type_of_vehicle
        self.speed = speed


        if self.name is 'Porshe' or 'Koenigsegg':
            self.doors = 2
        else:
            self.doors = 4

        if self.type_of_vehicle == 'trailer':
            self.wheels = 8
        else:
            self.wheels = 4

    def types_of_car(self):
        if self.type_of_vehicle != 'trailer':
            self.type_of_vehicle = 'saloon'

    def car_speed(moving_speed):
        if self.moving_speed == 3:
            self.speed == 1000
        elif self.moving_speed == 7:
            self.speed == 77
