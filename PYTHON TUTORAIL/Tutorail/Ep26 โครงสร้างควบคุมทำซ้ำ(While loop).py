# โครงสร้างควบคุมแบบทำซ้ำ While loop

'''
while   expression :
        statement
'''

i=1 # ตัวนับจำนวนรอบ

while i<=3: #1<=3 , 2<=3 , 3<=3
    print("รอบที่ ",i)
    i=i+1 # 2 , 3 , 4

print("จบโปรแกรม")

#example
w=1 # ตัวนับจำนวนรอบ
summation = 0 # เก็บผลการบวกเลขตามจำนวน #1+2+3+4+5
average = 0 # ผลรวม / จำนวนรอบ

count=int(input("ระบุจำนวนรอบ : "))
while w<=5:
        summation+=w # เก็บผลรวมชอง i แต่ละรอบ 1+2
        print("รอบที่ ",w," ค่า sum = ", summation)
        w+=1 #1,2,3,4,5

average = summation/10

print("ผลรวมการบวกเลข = ", summation)
print("ค่าเฉลี่ย = ", average)
