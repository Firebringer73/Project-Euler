def IsPent(n):
    Result=(1+(1+24*n)**(1/2))/(6)
    if Result==int(Result):
        return True
    return False

def IsHex(n):
    Result=(1+(1+8*n)**(1/2))/(4)
    if Result==int(Result):
        return True
    return False

def Tri(n):
    return((n/2)*(n+1))

Done=False
n=285
while not(Done):
    n+=1
    Triangle=Tri(n)
    if IsPent(Triangle) and IsHex(Triangle):
        print(int(Triangle))
        Done=True
