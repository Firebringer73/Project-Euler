def Pent(n):
    return int((n*(3*n-1))/2)

def IsPent(n):
    Result=(1+(1+24*n)**(1/2))/(6)
    if Result==int(Result):
        return True
    return False

minD=1000000000
n=0
while True:
    n+=1
    Pk=Pent(n)
    for i in range(1,n):
        Pj=Pent(i)
        if IsPent(Pk-Pj):
            if IsPent(Pk+Pj):
                if Pk-Pj<minD:
                    minD=Pk-Pj
                    print(minD)

