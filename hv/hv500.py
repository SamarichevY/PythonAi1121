class Людина:
    def __init__(self, імя, вік):
        self.імя = імя
        self.вік = вік
        self.робота = None

    def отримати_інформацію(self):
        print(f"Ім'я: {self.імя}, Вік: {self.вік}")
        if self.робота:
            print(f"Місце роботи: {self.робота.назва}")
        else:
            print("Безробітний")

class Робота:
    def __init__(self, назва):
        self.назва = назва

людина1 = Людина("Вася", 94)

робота1 = Робота("Офіс")

людина1.робота = робота1

людина1.отримати_інформацію()