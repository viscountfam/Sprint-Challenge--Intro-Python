# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# Vehicle is the base class
class Vehicle():
    pass

# Ground and Flight Vehicles are subclasses of the Vehicle class
class GroundVehicle(Vehicle):
   pass



class FlightVehicle(Vehicle):
   pass
# Car and Motorcycle would be subclasses of groundVehicle
class Car(GroundVehicle):
    pass
class Motorcycle(GroundVehicle):
    pass

# Starship and Airship would be subclasses of FlightVehicle
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass
