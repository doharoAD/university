from threading import Thread
from hashlib import md5
import time
from colorama import Fore

ts=int(input('Введите время(в сек): ')) 
class MyThread(Thread):
 
    def __init__(self, string:str):
        Thread.__init__(self)
        self.__stop = True
        self.__count = 0
        self.__hash = md5(string.encode())
 
    def run(self):
        self.__stop = False
        while not self.__stop:
            self.__hash = md5(self.__hash.digest())
            self.__count += 1
        
 
    def stop(self)->int:
        self.__stop = True
        return self.__count
 
 
th1 = MyThread("1234")
th2 = MyThread("12345")
th3 = MyThread("123456")
th4 = MyThread("1234567")

th1.start()
th2.start()
th3.start()
th4.start()
time.sleep(ts)

print('Колличество хешей 1-го ядра: ',th1.stop())
print('Колличество хешей 2-го ядра:',th2.stop())
print('Колличество хешей 3-го ядра: ',th3.stop())
print('Колличество хешей 4-го ядра: ',th4.stop())
print('Общее колличество хешей',(th1.stop()+th2.stop()+th3.stop()+th4.stop()))
print('Производительность процессора: ',((th1.stop()+th2.stop()+th3.stop()+th4.stop())//ts),'хеши/сек')



res=open('res.txt','a')
res.write(str('\n'))


res.write(str("Время выполнения программы"))
res.write(str(' - '))
res.write(str(ts))
res.write(str(' сек'))
res.write(str('\n'))
res.write(str('\n'))

res.write(str("Колличество хешей 1-го ядра"))
res.write(str(' - '))
res.write(str(th1.stop()))
res.write(str('\n'))

res.write(str("Производительность 1-го ядра"))
res.write(str(' - '))
res.write(str( th1.stop() //ts))
res.write(str(' хеши/сек'))
res.write(str('\n'))
res.write(str('\n'))

res.write(str("Колличество хешей 2-го ядра"))
res.write(str(' - '))
res.write(str(th2.stop() ))
res.write(str('\n'))

res.write(str("Производительность 2-го ядра"))
res.write(str(' - '))
res.write(str( th2.stop() //ts))
res.write(str(' хеши/сек'))
res.write(str('\n'))
res.write(str('\n'))

res.write(str("Колличество хешей 3-го ядра"))
res.write(str(' - '))
res.write(str(th3.stop() ))
res.write(str('\n'))

res.write(str("Производительность 3-го ядра"))
res.write(str(' - '))
res.write(str( th3.stop() //ts))
res.write(str(' хеши/сек'))
res.write(str('\n'))
res.write(str('\n'))

res.write(str("Колличество хешей 4-го ядра"))
res.write(str(' - '))
res.write(str(th4.stop() ))
res.write(str('\n'))

res.write(str("Производительность 4-го ядра"))
res.write(str(' - '))
res.write(str( th4.stop()//ts))
res.write(str(' хеши/сек'))
res.write(str('\n'))
res.write(str('\n'))

res.write(str("Общее колличество хешей"))
res.write(str(' - '))
res.write(str((th1.stop()+th2.stop()+th3.stop()+th4.stop()) ))
res.write(str('\n'))

res.write(str("Производительность процессора"))
res.write(str(' - '))
res.write(str( (th1.stop()+th2.stop()+th3.stop()+th4.stop()) //ts))
res.write(str(' хеши/сек'))
res.write(str('\n'))

res.write(str('#########################################'))
res.write(str('\n'))

res.close()

