import random as r
#cityMatrix = [[r.randrange(1,100,1) for j in range(5)] for i in range(5)]
f = open('text.txt')
cityMatrix = []
for line in f:
   row = [float(i) for i in line.split()]
   cityMatrix.append(row)
for i in range(6):
    # for i in range(5):
    #     for j in range(5):
    #         if(i==j):
    #             cityMatrix[i][j]=100
    #         if (j>i):
    #             cityMatrix[j][i]=cityMatrix[i][j]
    for i in cityMatrix:
        print(i)
    print("---" * 20, "\n")
    #X = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    X = [x for x in range(len(cityMatrix))]
    tempS = r.choice(X)
    X.remove(tempS)
    S = []
    Distance = 0
    S.append(tempS+1)
    print("City: ", tempS + 1,"\n","---"*20)
    while(X):
        Min = max(cityMatrix[tempS])
        for i in X:
            if(cityMatrix[tempS][i]<Min):
                Min = cityMatrix[tempS][i]
                indexMin = i
        print("City: ", indexMin + 1, "\n", "Distance: ",
              cityMatrix[tempS][indexMin],"\n","---"*20)
        Distance = Distance + cityMatrix[tempS][indexMin]
        tempS = indexMin
        X.remove(tempS)
        S.append(tempS+1)
    print("---"*20,"\n",S,"\nDistance: ",Distance)