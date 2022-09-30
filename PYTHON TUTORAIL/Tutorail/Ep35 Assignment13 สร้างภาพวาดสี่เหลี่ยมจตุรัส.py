#สร้างภาพวาดสี่เหลี่ยมจตุรัส

'''

3x3
xxx
xxx
xxx

2x2
xx
xx

5x5
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx

'''

number=int(input("ป้อนขนาด = "))

for row in range(number): #ถ้าไม่ระบุตัวเลขหน้า number จะเริ่มต้นที่ 0
    for column in range(number):
        print("X",end='')
    print(" ")
