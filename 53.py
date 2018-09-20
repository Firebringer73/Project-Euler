#Euler 53
def Factorial(N):
    if N<0:
        raise NameError("Factorial of less than 0 cannot be computed")
    elif N==0:
        return 1
    else:
        return N*Factorial(N-1)

def Choose(N,R):
    return int(Factorial(N)/(Factorial(R)*Factorial(N-R)))

def Run():
    Total=0
    for i in range(1,101):
        for j in range(0,i):
            if Choose(i,j)>1000000:
                Total+=1
    print(str(Total))

Run()
