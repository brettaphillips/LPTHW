# LCTHW - Exercise 4: Variables and Names
# by: Brett A Phillips
# Date: February 3, 2013

# Total number of cars in fleet
cars = 100
# Average number of passenger seats per car (float)
space_in_a_car = 4.0
# Total number of drivers in fleet
drivers = 30
# Total number of passangers today
passengers = 90
# Calculation (100 - 30)
cars_not_driven = cars - drivers
# Assume 1 driver per car
cars_driven = drivers
# Capacity = cars times average space (30 * 4.0) (FLOAT)
carpool_capacity = cars_driven * space_in_a_car
# Average number of actual people in cars today (90/3) (INTEGER DUE TO INPUTS)
average_passengers_per_car = float(passengers / cars_driven)

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We can have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."