#เกมทายเลขลูกเต๋า
#1,2,3,4,5,6

import random

#สุ่มเลขลูกเต๋า
myrandom=random.randrange(1,7) # สุ่ม 1-6
k=1
correct=False
print("คุณมีโอกาสตอบ 3 ครั้ง \n")
while True :
    number=int(input("ป้อนคำตอบของคุณ = "))
    correct=(number==myrandom) # True / Correct

    if not correct :
        if (number>myrandom):
            print("น้อยกว่า")
        if (number<myrandom):
            print("มากกว่า")
            
    if correct :
        print("ตอบถูกรับไปเลย 1 ล้าน Primogem")
        break
    if number<0 or k==3:
        break
    k+=1

if not correct :
    print("เสียใจด้วย")
    print("เฉลย = ",myrandom)
