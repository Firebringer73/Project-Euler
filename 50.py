def Sieve(Limit):
    Nums=list(range(2,Limit+1))
    Index=0
    while Index<len(Nums):
        Current=Nums[Index]
        Pointer=Index+Current
        while Pointer<len(Nums):
            Nums[Pointer]=0
            Pointer+=Current
        Index+=1
        try:
            while Nums[Index]==0 and Index<len(Nums):
                Index +=1
        except:
            pass
    Primes=[]
    for Num in Nums:
        if Num!=0:
            Primes.append(Num)
    return Primes

def IsPrime(Num):
    for i in range(2,int(Num**(1/2))+1):
        if Num % i==0:
            return False
    return True

def Run():
    MaxConsecutives=0
    Answer=0
    Primes=Sieve(10**6)
    print("done")
    for i in range(len(Primes)):
        Sum=Primes[i]
        Consecutives=1
        while Sum<1000000:
            Consecutives+=1
            Sum+=Primes[i+Consecutives-1]
            if IsPrime(Sum):
                if Consecutives>MaxConsecutives:
                    MaxConsecutives=Consecutives
                    Answer=Sum
                    print(Answer)

Run()
            
