def LongDiv(Num,Divisor):
    
    if Divisor==0:
        print("Fuck off with your zero division")
        return False
    
    Num=str(Num)
    OriginalLength=len(Num)
    IsDecimal= "." in Num
    Inspect=int(Num[:1])
    Result=""

    while len(Result)<5000:
        
        if (len(Result)==OriginalLength and not(IsDecimal)):
            Result+="."
        elif Num[0]==".":
            Num=Num[1:]
            Result+="."
        while len(Num)<=len(str(Divisor)):
            Num+="0"
            
        
        if Inspect>Divisor:
            Result+=str(Inspect//Divisor)
            Inspect=Inspect % Divisor
        else:
            Result+="0"
        Num=Num[1:]
        Inspect*=10
        Inspect+=int(Num[:1])
        #print("Inspect {}".format(Inspect))
        #print("Result {}".format(Result))
        #print("Num {}".format(Num))
    return Result

def Main():
    MaxLen=0
    Answer=-1
    for i in range(1,1000):
        if GetRepeatLength(LongDiv(1,i))>MaxLen:
            MaxLen=GetRepeatLength(LongDiv(1,i))
            Answer=i
    return Answer

def GetRepeatLength(String):
    for Start in range(2,5):
        for End in range(Start,len(String)):
            Length=End+1-Start
            if String[Start:End+1]==String[End+1:End+1+Length]==String[End+1+Length:End+1+Length+Length]:
                return Length
    return -1
Answer=Main()
print(Answer)
print(LongDiv(1,Answer))

