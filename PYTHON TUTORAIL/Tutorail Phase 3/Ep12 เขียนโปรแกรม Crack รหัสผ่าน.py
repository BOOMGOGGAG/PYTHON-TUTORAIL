#รหัส ATM = ko6
import random

ATM_PASSWORD="ko6"
result="" #สำหรับเก็บผลลัพท์

list_number=random.choice("0123456789")

print(list_number)

while result!=ATM_PASSWORD:
    result=""
    for letter in range(len(ATM_PASSWORD)):
        list_number=random.choice("0123456789abcdefghijklmnopqrstuvwsyz")
        result="".join(list_number)+str(result)
        print("SEARCH = ",result)
print("CRACK PASSWORD IS ",result)