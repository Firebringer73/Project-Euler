def ArePermutations(A,B):
    for Digit in A:
        if not(Digit in B):
            return False
    for Digit in B:
        if not(Digit in A):
            return False
    return True

def DigitSum(X):
    Sum=0
    for Digit in X:
        Sum+=int(Digit)
    return Sum

def DigitMultiply(X):
    Total=1
    for Digit in X:
        Total*=int(Digit)
    return Total

def CheckList(Data):
    for i in range(len(Data)):
        if not(ArePermutations(Data[0],Data[i])):
            return False
    return True

def Run():
    Current=1
    Done=False
    while not Done:
        Current+=1
        if CheckList([str(Current),str(Current*2),str(Current*3),str(Current*4),str(Current*5),str(Current*6)]):
            print(Current)
            Done=True

Run()
