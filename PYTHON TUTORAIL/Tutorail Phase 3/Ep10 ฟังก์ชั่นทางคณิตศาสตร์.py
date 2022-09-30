"""
#ค่าน้อยสุด
x=min(3,4,5,-10,30,40)
print(x)

#ค่ามากสุด
y=max(3,4,5,-10,30,40)
print(y)

#ค่าสัมบูรณ์
z=abs(-50)
print(z)

#ยกกำลัง
p=pow(5,2)
print(p)
"""

import math

#square root คือ รากที่... เช่น รากที่ 2 ของ 16 คือ 4
result=math.sqrt(64)
print(result)

#เศษ ปัดขึ้น
score=math.floor(80.4)
print(score) #80

#เศษ ปัดขึ้น
score1=math.ceil(80.4)
print(score1) #81

#ค่า π คือ 3.14....
print(math.pi)

#ค่าตรีโกณ sin,cos,tan (ค่าหน่วย degrees)
x=math.sin(30.00)
print(x)

#(ค่าหน่วย radians) ของ ตรีโกณ
convert=math.radians(90) # degrees => radians
x=math.sin(convert) #radians
print(x)

#ระยะทางจากจุด 2 จุด
point1=[2,-3]
point2=[7,-3]
#คำนวณระยะทางจากจุด 1 => จุด 2
d=math.dist(point1,point2)
print(d)

#ลอการิทึม เช่น log10 1000 = 3
l1=math.log10(1000)
print(l1)
#เช่น log2 32 = 5
l2=math.log2(32)
print(l2)

#ดูเพิ่มเติม ได้ที่
#https://www.programiz.com/python-programming/modules/math
#https://docs.python.org/3.11/library/math.html