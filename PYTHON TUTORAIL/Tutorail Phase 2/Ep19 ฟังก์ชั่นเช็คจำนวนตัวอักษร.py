# หาจำนวนตัวอักษรพิมพ์เล็ก/ใหญ่

# ABcDEfg

def checkSting(message):
    result={"UPPER":0,"LOWWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower():
            result["LOWWER"]+=1
        else :
            pass
    return result

x=checkSting("ABcDEfg")
print(x)