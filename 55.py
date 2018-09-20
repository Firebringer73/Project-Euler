#Euler 55
def IsPalindrome(String):
    i=0
    while i < int(len(String)/2) + 1:
        if String[i]!=String[-(i+1)]:
            return False
        i+=1
    return True

def Reverse(Integer):
    Current=str(Integer)
    Value=""
    for i in range(len(Current)):
        Value+=Current[-(i+1)]
    return int(Value)

def CheckNum(Integer):
    Counter=0
    while Counter<50:
        Counter+=1
        Integer+=Reverse(Integer)
        if IsPalindrome(str(Integer)):
            return True
    return False
        
def Run():
    Sum=0
    for i in range(1,(10**4)+1):
        if not(CheckNum(i)):
            Sum+=1
    print(Sum)

Run()
