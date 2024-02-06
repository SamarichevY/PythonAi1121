class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.home = None

    def move_in(self, home):
        self.home = home
        print(f"{self.name} переїхав у свій новий дім.")

    def interact_with_home(self):
        if self.home:
            print(f"{self.name} взаємодіє з домом.")
        else:
            print(f"{self.name} не має дому для взаємодії.")


class Home:
    def __init__(self, address):
        self.address = address
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)
        print(f"{resident.name} тепер проживає за адресою {self.address}.")

person1 = Human("діма", 22)
person2 = Human("антон", 21)

home1 = Home("вул. Перша, 1")
home2 = Home("вул. Друга, 2")

person1.move_in(home1)
person2.move_in(home2)

person1.interact_with_home()
person2.interact_with_home()