import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.satiety = 40
        self.happiness = 40
        self.is_sleeping = False

    def limits(self):
        if self.satiety > 100:
            self.satiety = 100

        if self.satiety < 0:
            self.satiety = 0

        if self.happiness > 100:
            self.happiness = 100

        if self.happiness < 0:
            self.happiness = 0

    def feed(self):
        if self.is_sleeping:
            return

        self.satiety += 15
        self.happiness += 5

        if self.satiety >= 100:
            self.happiness -= 30

        self.limits()

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness -= 5
            self.limits()
            return

        angry = random.randint(1, 3)

        if angry == 1:
            self.happiness = 0
        else:
            self.happiness += 15
            self.satiety -= 10
            
        self.limits()

    def sleep(self):
        self.is_sleeping = True