import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow",12)

print(primrose.get_color())

# methods of the supertype are inherited by the subtype
print(sunflower.get_color())
print(sunflower.get_petals())

# you cannot use a method of a subtype for a supertype
# print(primrose.get_petals())
