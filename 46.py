def IsPrime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

n=1
Done=False
while not(Done):
    n+=2
    if not(IsPrime(n)):
        Holds=False
        i=1
        while 2*i**2<n:
            if IsPrime(n-2*i**2):
                Holds=True
            i+=1
        if not(Holds):
            Done=True
            print(n)
