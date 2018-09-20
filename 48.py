#Euler problem 48
def PseudoPower(Num):
    Count=0
    Result=1
    while Count<Num:
        Count+=1
        Result*=Num
    return Result
print(PseudoPower(6))
Sum=0
for i in range(1,1001):
    Sum+=PseudoPower(i)
print(Sum)
