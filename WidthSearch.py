import Util as u, random as r,numpy as np, operator
import sys
def widthSearch():
    # m это словарь, где ключом является кодировка, а значением функция приспособленности
    m = u.EncodingsValues
    # for q in m:
    #     #sys.stdout.write(m[q])
    #     print(m[q],end=',')
    # print('\n')
    # j = 0
    # while(j<5):
    i = 0
    si = r.choice(list(m.keys()))
    currentS=si
    Max = m[currentS]
    #новый словарь с расстоянием хэмминга равным 1
    field = u.field(m, si)
    while i<5:
        # print(i+1,")\nCurrentS = ", u.intToNArray(si))
        # print("CurrentMax = ", Max)
        # print("Field:")
        #u.printField(field)
        #print("---" * 20)
        #набор у которого макс ф-ия приспособленности в данной сигме
        Sk = max(field.items(), key = operator.itemgetter(1))[0]
        #ключ с максимальным значением в словаре
        if m[Sk] > Max:
            # print("     MaxS = ", u.intToNArray(Sk))
            # print("     Max:", Max, "-> ", m[Sk])
            # print("---" * 20)
            Max = m[Sk]
            currentS = Sk
            field = u.field(m, currentS)
        else:
            break
        i = i+1
        #print("---"*20)
        print("S = ",u.intToNArray(currentS))
        print("Max = ",Max)
        return (currentS,Max)
        # j=j+1