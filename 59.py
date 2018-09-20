def Crypt(CipherText,Password):
    Key=""
    Result=""
    while len(Key)<len(CipherText):
        Key+=Password
    for i in range(len(CipherText)):
        Result+=chr(ord(CipherText[i])^ord(Key[i]))
    return Result
def GetCipherText():
    with open("59Text.txt","r") as File:
        Contents=File.read().split(",")
        Contents=list(map(lambda x: chr(int(x)), Contents))
        Contents="".join(Contents)
    return Contents
def Decrypt():
    CipherText=GetCipherText()
    for i in range(97,123,1):
        for j in range(97,123,1):
            for k in range(97,123,1):
                PlainText=Crypt(CipherText,str(chr(i)+chr(j)+chr(k)))
                if "and " in PlainText and "the " in PlainText:
                    return PlainText
    return False
def AsciiSum(Text):
    Result=0
    for Char in Text:
        Result+=ord(Char)
    return Result
print(AsciiSum(Decrypt()))
