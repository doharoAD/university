# использование полиморфизма
class Lodka:
    def plavaet(self):
        print("Лодка плавает")
    def letaet(self):
        print("Лодка не летает")

class Samolet:
    def plavaet(self):
        print("Самолёт не плавает")
    def letaet(self):
        print("Самолёт летает")
    # общий интерфейс
    def test_plav(Lodka):
        Lodka.plavaet()


if __name__ == "__main__":
    
    # создаём экзепляры класса
    lodka1 = Lodka()
    samolet1 = Samolet()

    # передача объектов в качестве аргумента
    
    #этот способ более "костыльный", это если подгонять под пример вывода
    print("----------------Способ 1----------------")
    lodka1.plavaet()
    samolet1.plavaet()
    
    #этот способ более правильный будет
    
    print("----------------Способ 2----------------")
    for machin in (lodka1, samolet1):
        machin.plavaet()
        machin.letaet()