# d = {2:3, 3:4, 1:1}
# max_value = max(list(d.values()))
# print(max_value)
# print(max([3,2]))
# #print(list(d.values()))
# import operator
# stats = {"a":1000, "b":3000, "c": 100, "d":3000}
# print(max(d.items(), key=operator.itemgetter(1))[0])
# print("---"*20)
# s = [1,2,3,4,5]
# s.insert(2,88)
# print(s)
# print(len(s))
# f = open('text.txt')
# out = []
# for line in f:
#    row = [float(i) for i in line.split()]
#    out.append(row)
# import random as r
# s = 0
# q = [x for x in range(1, 100)]
# for i in range(100):
#    if r.choice(q) in q[45:55]:
#       s = s + 1
# print(s)
f = open('forKnapsack.txt')
cityMatrix = []
for line in f:
   row = [int(i) for i in line.split()]
   cityMatrix.append(row)
print(cityMatrix)
W = []
Q = []
for i in cityMatrix:
   W.append(i[1])
   Q.append(i[2])
print(W)
print(Q)
