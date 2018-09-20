def IsNgonal(N,x):
    Test=((((8*N-16)*x+((N-4)**2))**(1/2))+N-4)/(2*N-4)
    if Test.is_integer():
        return True
    return False
def CreateLists(UpperLimit):
    for N in range(3,UpperLimit+1):
        PolyNums.append([])
        for x in range(1000,10000):
            if IsNgonal(N,x):
                PolyNums[N-3].append(x)
            
        
    
def Main():
    CreateLists(8)
    for List in PolyNums:
        print(List)
PolyNums=[]
Main()

