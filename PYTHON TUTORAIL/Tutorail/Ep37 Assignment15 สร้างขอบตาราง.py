#สร้างขอบตาราง

number=int(input("ป้อนขนาด = "))

for row in range(number): #ถ้าไม่ระบุตัวเลขหน้า number จะเริ่มต้นที่ 0
    for column in range(number):
        if row == 0 or row == number-1 or column == 0 or column == number-1:
            print("x",end='')
        else :
            print(" ",end='')
    print(" ")