sumW = 0
Wmax = 50
Q = 0
f = open('forKnapsack.txt')
temp = []
for line in f:
   row = [int(i) for i in line.split()]
   temp.append(row)
W = []
C = []
for i in temp:
   W.append(i[1])
   C.append(i[2])
S = [0]*len(W)
Y = [round(C[i]/W[i],4) for i in range(len(C))]
while True:
    y = max(Y)
    indexY = Y.index(y)
    if sumW+W[indexY] > Wmax:
        break
    sumW = sumW + W[Y.index(y)]
    Q = Q + C[indexY]
    print(Y)
    print(S)
    print(W[indexY])
    print('---' * 20)
    S[indexY] = 1
    Y[indexY] = 0
print('---'*20, '\n', S, '\n', '---'*20, '\nQ = ', Q, '; sumW = ', sumW)







