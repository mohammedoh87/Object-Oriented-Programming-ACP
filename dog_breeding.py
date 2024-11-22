class dog:
    animal = "mammal"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

roble = dog("Roble", "pitbull")
deero = dog("Deero", "bulldog")
print("Roble is a {}".format(roble.animal))
print("Deero is a {}".format(deero.animal))

print("{} is fromthe {} breed of dogs".format(roble.name, roble.breed))
print("{} is from the {} breed of dogs".format(deero.name, deero.breed))