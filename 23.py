def GetFactorSum(Num):
    Total=1
    for i in range(2,int(Num**(1/2))+1):
        if Num%i==0:
            Total+=i
            OtherFactor=int(Num/i)
            if OtherFactor!=i:
                Total+=OtherFactor
    return Total
def IsAbundant(Num):
    if GetFactorSum(Num)>Num:
        return True
    return False

def Main():
    Sum=0
    Abundants=[]
    for i in range(1,28123):
        Expressible=False
        for Item in Abundants:
            if IsAbundant(i-Item):
                Expressible=True
                break
        if not(Expressible):
            Sum+=i
        if GetFactorSum(i)>i:
            Abundants.append(i)
        if i%1000==0:
            print(int(i/1000))
    print(Sum)

Main()
