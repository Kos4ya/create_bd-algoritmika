from random import *
import os

for i in range(int(input("количество файлов: "))):
    f = open("BD/"f"{input('введите имя')}.txt", "w")
    f.write(str(randint(1, 1000)))
    f.close()

for i in os.walk("BD"):
    for j in i[2]:
        f = open(f"BD/{j}", "r")
        c = f.read()
        print(c)
        f.close()

for i in os.walk("BD"):
    for j in i[2]:
        os.remove(f"BD/{j}")
