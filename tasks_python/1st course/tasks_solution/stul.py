# Используем инкапсуляцию данных
class Computer:

    def __init__(self):
        self.__maxcena = 200

    def magazin(self):
        print("Цена продажи: {}".format(self.__maxcena))

    def setmaxcena(self, sum):
        self.__maxcena = sum

if __name__ == "__main__":

    s = Computer()
    s.magazin()

    # изменение цены
    s.setmaxcena(800)
    s.magazin()

    # используем функцию изменения цены
    s.setmaxcena(1000)
    s.magazin()