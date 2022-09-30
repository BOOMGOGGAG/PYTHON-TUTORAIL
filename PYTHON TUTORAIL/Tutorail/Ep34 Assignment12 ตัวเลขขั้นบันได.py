#ตัวเลขขั้นบันได

'''
input = 4

1
12
123
1234

'''

last=int(input("ป้อนตัวเลข = "))

for row in range(1,last+1):#เริ่มต้นที่ 1
    for column in range(1,row+1):#เริ่มต้นที่ 2
        print(column,end='') #ตัว end='' ทำให้เป็นแนวนอน
    print(" ") # ขึ้นบรรทัดใหม่

'''
input = 3

row = 1 ,1+2
column = 1 จนถึงก่อน 1+1(1 จนถึงก่อน 2)

1

row = 2
column = 1 จนถึงก่อน 2+1(1 จนถึงก่อน 3)

12

row = 3
column = 1 จนถึงก่อน 3+1(1 จนถึงก่อน 4)

123

'''