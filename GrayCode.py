import Util as u, random as r,numpy as np, operator
import sys
# m это словарь, где ключом является кодировка, а значением функция приспособленности
m = {x:np.random.randint(0,900) for x in range(0,32)}
print(m)
i = 0
si = r.choice(list(m.keys()))
currentS=si
Max = m[currentS]
#новый словарь с расстоянием хэмминга равным 1
field = u.field(m, u.getGrayCode(si))
while i<5:
    print(i+1,")\nCurrentS = ", u.intToNArray(si))
    print("CurrentMax = ", Max)
    print("Field:")
    u.printField(field)
    print("---" * 20)
    #набор у которого макс ф-ия приспособленности в данной сигме
    Sk = max(field.items(), key = operator.itemgetter(1))[0]
    #ключ с максимальным значением в словаре
    if m[Sk] > Max:
        print("     MaxS = ", u.intToNArray(Sk))
        print("     Max:", Max, "-> ", m[Sk])
        print("---" * 20)
        Max = m[Sk]
        currentS = Sk
        field = u.field(m, u.getGrayCode(currentS))
    else:
        break
    i = i+1
print("---"*20)
print("S = ",u.intToNArray(currentS))
print("Max = ",Max)