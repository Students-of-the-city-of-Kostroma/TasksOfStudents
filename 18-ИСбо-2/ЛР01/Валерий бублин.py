import random  # подключение библиотеки
from random import randint

n = 10
x = 5
mas = [randint(1, 10) for i in range(n)]  # инициализируем массив

u = 0
while u < n and mas[u] != x:  # если элемент не равен
    u += 1
if u < n:
    print("mas[", u, "]=", x, sep="")
else:
    print("Не нашли!")