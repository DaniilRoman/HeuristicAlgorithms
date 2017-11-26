import Util as u, random as r, numpy as np
def deepSearch():
    # m это словарь, где ключом является кодировка, а значением функция приспособленности
    m = u.EncodingsValues
    i = 0
    si = r.choice(list(m.keys()))
    currentS=si
    Max = m[currentS]
    #новый сет с элементами равными 1 растояния хэмминга
    field = u.field(m, si)
    while i<5 and field:
        # print(i,")\nCurrentS = ",u.intToNArray(si))
        # print("CurrentMax = ",Max)
        # print("Field:")
        #u.printField(field)
        #print("---"*20)
        #выбор соучайного ключа в field
        si = r.choice(list(field.keys()))
        if field[si] > Max:
            # print("     MaxS = ", u.intToNArray(si))
            # print("     Max:", Max, "-> ", field[si])
            # print("---" * 20)
            Max = field[si]
            currentS = si
            #строим новое множество соседей
            field = u.field(m, si)
        else:
            #удаляем элемент si из нашего множества соседей
            field.pop(si)
        i = i+1
    #print("---"*20)
    print("MaxS = ",u.intToNArray(currentS))
    print("Max = ",Max)
    return (currentS,Max)