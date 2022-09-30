# function input
name=input("กรุณาป้อนชื่อของท่าน : ")#รับค่าที่ผู้ใช้ป้อนแล้วเก็บลงตัวแปร name
lname=input("กรุณาป้อนนามสกุล : ")
print("ชื่อของคุณ = "+name)
print("นามสกุลของคุณ = "+lname)
print(type(name))

#input(รูปแบบที่ 2)
x=input("ป้อนตัวเลขตัวที่ 1 : ")#รับค่าที่ผู้ใช้ป้อนแล้วเก็บลงตัวแปร name
y=input("ป้อนตัวเลขตัวที่ 2 : ")

#process
z=int(x)+int(y)

#output
print(z)

#input(รูปแบบที่ 3)
x=int(input("ป้อนตัวเลขตัวที่ 1 : "))#รับค่าที่ผู้ใช้ป้อนแล้วเก็บลงตัวแปร name
y=int(input("ป้อนตัวเลขตัวที่ 2 : "))

#process
z=x+y

#output
print(z)

#process & output(รูปแบบที่ 4)
print(x+y)