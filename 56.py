def GCD(a,b): #returns the GCD of a and b
    if a==b:
        return a
    else:
        if a>b:
            return GCD(b,(a-b))
        else:
            return GCD(b,(b-a))

def CancelFraction(Num,Den):
    #Cancel=GCD(Num,Den)
    return (Num,Den)

def AddIntAndFraction(Int,Num,Den):
    return CancelFraction(int(Int)*int(Den)+int(Num),int(Den))

def AddFraction(Num1,Den1,Num2,Den2):
    return CancelFraction(int(Num1*Den2+Num2*Den1),int(Den1*Den2))

def FlipFraction(Num,Den):
    return (Den,Num)

def Run():
    Num=0
    Den=1
    Count=0
    for i in range(1000):
        Num,Den = FlipFraction(AddIntAndFraction(2,Num,Den)[0],AddIntAndFraction(2,Num,Den)[1])
        Result=AddIntAndFraction(1,Num,Den)
        #print(str(Result[0])+"/"+str(Result[1]))
        if len(str(Result[0]))>len(str(Result[1])):
            #print("")
            Count+=1
    print("Answer is : " +str(Count))
Run()
