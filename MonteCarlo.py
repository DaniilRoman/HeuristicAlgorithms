import random as r, Util as u, numpy as np
def monteCarlo():
    # m это словарь, где ключом является кодировка, а значением функция приспособленности
    m = u.EncodingsValues
    i = 0
    #выбор рандомного ключа из нашего m
    # currentS=r.choice(list(m.keys()))
    # Max = m[currentS]
    currentS =0;
    Max = 0;
    while i < 5:
        s = r.choice(list(m.keys()))
        # print(i, ")\nCurrentS = ", u.intToNArray(s))
        # print("CurrentFitness = ", m[s])
        # print("---" * 20)
        if m[s]>Max:
            # print("     MaxS = ", u.intToNArray(s))
            # print("     Max:",Max,"-> ", m[s])
            # print("---" * 20)
            Max = m[s]
            currentS = s
        i = i+1
    #print("---"*20)
    print("MaxS = ",u.intToNArray(currentS))
    print("Max = ",Max)
    return (currentS,Max)