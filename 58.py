def IsPrime(Num):
    if Num<1:
        return False5
    for i in range(2,int(Num**(1/2))+2):
        if Num % i == 0:
            return False
    return True

def AddLayer(Pointer,SideLength,TotalNums,TotalPrimes):
    for i in range(4):
        Pointer+=(SideLength+1)
        if IsPrime(Pointer):
            TotalPrimes+=1
        TotalNums+=1
    SideLength+=2
    return (Pointer,SideLength,TotalNums,TotalPrimes)

TotalNums=1
TotalPrimes=0
SideLength=1
Pointer=1
Done=False
while not(Done):
    Pointer,SideLength,TotalNums,TotalPrimes=AddLayer(Pointer,SideLength,TotalNums,TotalPrimes)
    #print()
    try:
        #print(str(SideLength) + " : " + str(TotalPrimes/TotalNums))
        Done=False
    except:
        pass
    if TotalPrimes/TotalNums<0.1:
        print(SideLength)
        Done=True
