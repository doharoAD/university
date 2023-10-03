class Cat:
    #атрибуты класса
    species = "кот"
    #атрибуты экземпляра
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # создаём методы экземпляра: myauk (мяукает) и spit (спит)
    def myauk(self, mya):
        return "{} мяукает {}".format(self.name,mya)
    def spit(self):
        return "{} спит ".format(self.name)
# cоздаём экземпляр класса
if __name__=="__main__":
    barsik = Cat("Барсик ", 5)

    # доступ к атрибутам экземпляра
    print("Возраст: {} – {} лет".format(barsik.name, barsik.age))

    # вызываем методы экземпляра
    print(barsik.myauk("тихо"))
    print(barsik.spit())
