def IsPrime(Num):
    if Num<2:
        return False
    for i in range(2,int(Num**(1/2))+1):
        if Num % i == 0:
            return False
    return True

def CheckThing(Nums):
    for i in range(len(Nums)):
        for j in range(i+1,len(Nums)):
            if not(IsPrime(int(str(Nums[i])+str(Nums[j])))):
                   return False
            if not(IsPrime(int(str(Nums[j])+str(Nums[i])))):
                   return False
    return True
                   
def CheckLists(Num):
    for Prime in Primes:
        Pair=[Num]+[Prime]
        if CheckThing(Pair):
            for P in Pairs:
                Triplet=[Num]+P
                if CheckThing(Triplet):
                    for T in Threes:
                        Quadruplet=[Num]+T
                        if CheckThing(Quadruplet):
                            Fours.append(Quadruplet)
                            for Quad in Fours:
                                Quint= [Num]+Quad
                                if CheckThing(Quint):
                                    Fives.append(Quint)
                    Threes.append(Triplet)
            Pairs.append(Pair)
    Primes.append(Num)

def Run():
    Counter=3
    Done=False
    while not(Done):
        if IsPrime(Counter):
            print(Counter)
            CheckLists(Counter)
        Counter+=2
        if len(Fives)!=0:
            Done=True
            print(Fives[0])

Primes=[2]
Pairs=[]
Threes=[]
Fours=[]
Fives=[]
Run()

        
