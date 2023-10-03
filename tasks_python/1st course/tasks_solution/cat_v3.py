class Cat:
    def __init__(self):
        print("Кот – любимое создание")

    def who(self):
        print("Кот ")
        
    def myauk(self):
        print("мяукает тихо")

# дочерний класс

class Siam(Cat):
    def __init__(self):

        # вызов функции super()

        super().__init__()
        print("Сиамский кот – любимое создание")
        
    def who(self):
        print("Сиамский кот: ")
        
    def spit(self):
        print("спит сладко")
        
if __name__ == "__main__":
    d = Siam()
    d.who()
    d.myauk()
    d.spit()
