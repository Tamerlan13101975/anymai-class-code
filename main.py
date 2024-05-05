

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
        print(f"Зоосмотритель {self.name} кормит животное {animal.name}")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")


    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит животное {animal.name}")


    def save_zoo_info(zoo, filename):
        with open(filename, "w") as f:
            zoo_data = {"animals": [], "employees": []}
            for animal in zoo.animals:
                zoo_data["animals"].append({"name": animal.name, "age": animal.age})
            for employee in zoo.employees:
                zoo_data["employees"].append({"name": employee.name, "role": employee.role})
            json.dump(zoo_data, f)

    def load_zoo_info(filename):
        with open(filename, "r") as f:
            zoo_data = json.load(f)
        zoo = Zoo()
        for animal_data in zoo_data["animals"]:
            animal = Animal(animal_data["name"], animal_data["age"])
            zoo.add_animal(animal)
        for employee_data in zoo_data["employees"]:
            employee = Employee(employee_data["name"], employee_data["role"])
            zoo.add_employee(employee)
        return zoo














