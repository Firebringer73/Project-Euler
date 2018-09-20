def IsPrime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

def NumPrimeFactors(n):
    List=[]
    while not(IsPrime(n)):
        Count=1
        Found=False
        while not(Found):
            Count+=1
            if n%Count==0:
                n=n/Count
                if not(Count in List):
                    List.append(Count)
                Found=True
    List.append(int(n))
    return len(List)
def Main():
    Consecutives=0
    n=0
    while Consecutives<4:
        n+=1
        if NumPrimeFactors(n)==4:
            Consecutives+=1
        else:
            Consecutives=0
    print(n-3)
Main()
