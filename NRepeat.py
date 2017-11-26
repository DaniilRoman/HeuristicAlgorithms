import MonteCarlo, DeepSearch, WidthSearch, math, Util, random
print(Util.EncodingsValues)
methods = {0:lambda:MonteCarlo.monteCarlo(),
           1:lambda:DeepSearch.deepSearch(),2:lambda:WidthSearch.widthSearch()}
names = {0:"Monte-Carlo", 1:"DeepSearch", 2:"WidthSearch"}
i = 0
Max = 0
MaxS = 0
currentMax = 0
currentMaxS = 0
while(i < 5):
    k = random.randrange(0,3,1)
    i = i+1
    print("\n",names[k])
    (currentMaxS,currentMax) = methods[k]()
    print("---"*20)
    if(currentMax>Max):
        Max = currentMax
        MaxS = currentMaxS
print("---"*20,"\n","---"*20,"\n","---"*20,"\n","Max: ",Max,"\nMaxS: ",Util.intToNArray(MaxS))