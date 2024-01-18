class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} мяу")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} мяу")

class Bird(Animal):
    def __init__(self, name, feather_color):
        super().__init__(name)
        self.feather_color = feather_color

    def lay_eggs(self):
        print(f"{self.name} мяу")

dog = Mammal("котяра", "Коричневий")
sparrow = Bird("кіт", "Сірий")

dog.make_sound()
dog.give_birth()

sparrow.make_sound()
sparrow.lay_eggs()