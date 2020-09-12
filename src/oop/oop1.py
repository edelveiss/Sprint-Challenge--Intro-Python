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
class Vehicle: #parent/base/super class for all those classes
    pass
class FlightVehicle(Vehicle): #Base class for Starship and Airplane
    pass
class Starship(FlightVehicle): #Child class for FlightVehicle
    pass
class GroundVehicle(Vehicle): #Base class for Car and Motorcycle
    pass
class Car(GroundVehicle): #Child class for GroundVehicle
    pass
class Motorcycle(GroundVehicle): #Child class for GroundVehicle
    pass
class Airplane(FlightVehicle): #Child class for FlightVehicle
    pass



