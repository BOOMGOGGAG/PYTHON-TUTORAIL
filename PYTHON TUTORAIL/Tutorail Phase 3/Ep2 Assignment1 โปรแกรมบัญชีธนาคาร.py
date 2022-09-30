#โปรแกรมบัญชีธนาคาร

#data
account={"นายA":5000,"นายB":0}

def getBalance():
    print("ยอดเงินคงเหลือในบัญชี :",account)

def deposit(money):
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ฝากเงินเข้สบัญชี A :",money)
    account["นายA"]+=money

def withdraw(money):
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ยอดเงินบัญชีไม่พอ")
    print("ถอนเงินจากบัญชี A :",money)
    account["นายA"]-=money

def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ป้อนตัวเลขเท่านั้นนะครับ")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ยอดเงินบัญชีไม่พอ")
    print("ทำการโอนเงินไปทีบัญชี B :",money)
    account["นายB"]+=money
    account["นายA"]-=money

try :
    getBalance()
    transfer(5001)
    getBalance()
except Exception as e :
    print(e)