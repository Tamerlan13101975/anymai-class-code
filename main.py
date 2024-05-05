class Animal:
    def __init__(self, name, age):
        self.name = name
        self. age = age

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Zoo:
    def __init__(self):
        self.animals = []
        self.employeed = []
    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employye(self, employee):
        self.employees.append(employee)


class ZooKeeper(Employee):
    def __init__(self, name):
        super(). __init__(name, "Zookeeper")


    def feed_animal(self, animal):
        print(f"Зоосмотритель {self, name} кормит животное {animal, name}")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")














