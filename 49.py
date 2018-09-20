def Run():
    for a in range(1,10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    test(str(a)+str(b)+str(c)+str(d))
def PrimesList():
    Primes=[]
    for i in range(1001,10000,2):
        if IsPrime(i):
            Primes.append(i)
    return Primes

def IsPerm(Str1,Str2):
    for letter in Str1:
        if not letter in Str2:
            return False
    for letter in Str2:
        if not letter in Str1:
            return False
    return True

def IsPrime(Num):
    for i in range(2,int(Num**(0.5)+1)):
        if Num % i == 0:
            return False
    return True

def FindSequences(Primes):
    for i in range(len(Primes)):
        for j in range(i+1,len(Primes)):
            JPrime=Primes[j]
            IPrime=Primes[i]
            Diff=JPrime-IPrime
            if IsPrime(JPrime+Diff) and len(str(JPrime+Diff))<5 and IsPerm(str(IPrime),str(JPrime)) and IsPerm(str(IPrime),str(JPrime+Diff)):
                print(str(IPrime)+" "+str(JPrime)+" "+ str(JPrime+Diff))

print(FindSequences(PrimesList()))
