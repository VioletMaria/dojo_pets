class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 250000

    def sleep(self):
        print(f"{self.name} is sleeping...")
        return self

    def eat(self):
        print(f"{self.name} is having num nums.")
        return self

    def play(self):
        print(f"{self.name} is digging in the garden for fun!")
        return self

    def noise(self):
        print(f"{self.name} is waking up the neighbors again...")
        return self

class Ninja:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = "biscuits"
        self.pet_food = "burger"
        self.pet = Pet("Chungy", "Dog", "backflip")

    def walk(self):
        print(f"Walking {self.pet.name}")
        return self

    def feed(self):
        print(f"Feeding {self.pet.name} {self.treats}")
        return self

    def bathe(self):
        print(f"Giving {self.pet.name} a bubble bath!")
        return self

alex = Ninja("Alex", "Jones")
alex.walk().feed().bathe()