def GetPermutations(Str):
    if len(Str)==1:
        return [Str]
    else:
        Str=list(Str)
        Perms=[]
        for i in range(len(Str)):
            CurrentDigit=Str[i]
            del Str[i]
            for Permutation in GetPermutations("".join(Str)):
                Perms.append(CurrentDigit+Permutation)
            Str.insert(0,CurrentDigit)
        return Perms

def Run():
    Sum=0
    Permutations=GetPermutations("0123456789")
    #print(len(Permutations))
    for Num in Permutations:
        if SatisfiesCondition(Num):
            Sum+=int(Num)
    print(Sum)

def SatisfiesCondition(NumStr):
    if len(NumStr)!=10:
        NumStr
    for i in range(7):
        Current=""
        for j in range(3):
            Current+=NumStr[i+j+1]
        #print(Current + "/" + str(Primes[i]))
        if int(Current) % Primes[i] != 0 :
            #print(int(Current) % Primes[i])
            return False
    return True
Primes=[2,3,5,7,11,13,17]
Run()
