# Create an empty set named showroom.
showroom = set()

# Add four cars models to the set.
showroom.add("VW Golf")
showroom.add("Audi TT")
showroom.add("Tesla Model 3")
showroom.add("VW Beetle")

# Print the length of your set.
print("Number of cars in showroom", len(showroom))

# Use update to add two more cars
showroom.update({"Audi Q3", "BMW X2"})

# You've sold a car. Remove it with discard()
showroom.discard("Tesla Model 3")

# Create a junkyard and include some overlap with showroom
junkyard = {"VW Golf", "VW Tiguan", "Volvo C30"}

# Acquire the cars in the junkyard you don't already have
cars_acquired = junkyard.difference(showroom)
showroom = showroom.union(cars_acquired)

for car in cars_acquired:
    junkyard.discard(car)


