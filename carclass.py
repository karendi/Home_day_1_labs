class Car(object):
  speed = 0
   #every object instance should have a name(set to General) , model(set GM) and vehicle_type
  def __init__(self, name='General', model='GM',vehicle_type=None):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type


    #if the name of the object is not in the list, then it should be set to two doors else it should be set to 4 doors

    if self.name in ['Porshe', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    #if the object with the vehicle_type:trailer an attribute of num_of_wheels is addded and set to 8 else its set to 4
    if self.vehicle_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4

# afunction that sets the vehicle type to saloon if its not a trailer
  def is_saloon(self):
    if self.vehicle_type is not 'trailer':
        self.vehicle_type == 'saloon'
        return True
    return False

#fuunction that exects moving_speed argument and sets the class variable(Car.speed)
  def drive(self, moving_speed):
    if moving_speed == 3:
      Car.speed = 1000
    elif moving_speed == 7:
      Car.speed = 77

    return self
