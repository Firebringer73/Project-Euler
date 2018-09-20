def Factorial(n):
    if n==1:
        return 1
    return n*Factorial(n-1)

def Main():
    Total=1000000
    final=""
    while Total!=0:
        for Num in Digits:
            if Total-2*Factorial(len(Digits)-1)<0:
                final+=str(Num)
                Digits.remove(Num)
                print(Num)
                print(Total)
                break
            else:
                Total-=Factorial(len(Digits)-1)
        print(final)

Digits=[0,1,2,3,4,5,6,7,8,9]
Main()
