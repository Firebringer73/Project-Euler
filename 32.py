def IsPandigital(Str):
    Multiplied=1
    Sum=0
    if len(Str)!=9:
        return False
    Str=list(Str)
    Digits=[]
    for i in range(9):
        Digits.append(str(i+1))
    for Digit in Str:
        try:
            Digits.remove(Digit)
        except:
            pass
    if len(Digits)==0:
        return True
    return False

def Run():
    Answers=[]
    Sum=0
    First=1
    Terminate=False
    while not(Terminate):
        First+=1
        Second=First-1
        Skip=False
        while not(Skip):
            Second+=1
            Product=First*Second
            Result=str(First)+str(Second)+str(Product)
            if IsPandigital(Result) and not(Product in Answers):
                print(str(First)+ "*" +str(Second)+"="+str(Product))
                Sum+=Product
                Answers.append(Product)
            if len(Result)>9:
                Skip=True
        if len(str(First))>4:
            Terminate=True
    print(Sum)

Run()
        
