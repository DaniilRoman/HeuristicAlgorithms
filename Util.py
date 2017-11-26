import numpy as np
from math import *
import os.path as o
#словарь, где ключом является кодировка, а значением функция приспособленности
EncodingsValues = {x:(5*sin(x)+log2(x)) for x in range(1, 2**7+1)}
def hammingDistance(a, b):
    #на вход подается 2 числа
    #числа превращаем в интовые массивы бит
    a = np.array(list('{0:05b}'.format(a)),  dtype=int)
    b = np.array(list('{0:05b}'.format(b)),  dtype=int)
    #возвращаем число отличающихся бит т.е. Хэмминговое растояние
    return np.count_nonzero(a!=b)
    #подается исходный set с si и значением функции приспособленности 
    #и номер с которм бцдем считать хэминговое расстояние
def field(map_, num):
    dictionary = {}
    for n in map_:
        if hammingDistance(num ,n)==1:
            dictionary.update({n:map_[n]})
    return dictionary
def intToNArray(si):
    return np.array(list('{0:05b}'.format(si)),  dtype=int)
def printField(field):
    for i in field:
        print(intToNArray(i),":::",field[i])
def getGrayCode(s):
    return s^(s>>1)
def grayCodeToBinCode(s):
    b = s
    for i in range(4):
        b = b^(s>>i+1)
    return b

