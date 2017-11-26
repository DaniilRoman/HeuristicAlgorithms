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
while True:
    c = max(C)
    indexC = C.index(c)
    if sumW+W[indexC] > Wmax:
        break
    sumW = sumW + W[C.index(c)]
    Q = Q + c
    print(C)
    print(S)
    print('Вес: ',W[indexC])
    print('---'*20)
    S[indexC] = 1
    C[indexC] = 0
print('---'*20, '\n', S, '\n', '---'*20, '\nQ = ', Q, '; sumW = ', sumW)











