# 1.การนิยาม,constructor

#มี 'ค่าหลายค่า' 'ข้อมูลต่างชนิดกัน' ได้ในตัวแปรเดียว ทั้ง Tuble&List เหมือนกัน
tup=(1,2,3,4,"kongruksiam","มะม่วง",True,3.99) #Tuble
lis=[1,2,3,4,"kongruksiam","มะม่วง",True,3.99] #List
print(tup)
print(lis)
#OR
tup=tuple((1,2,3,4,"kongruksiam","มะม่วง",True,3.99)) #Tuble
lis=list([1,2,3,4,"kongruksiam","มะม่วง",True,3.99]) #List
print(tup)
print(lis)

#ความแตกต่าง ระหว่าง Tuble&List
#lis[0]="กรุงเทพ"#แก้ไขข้อมูลได้
#tup[0]="กรุงเทพ"#ไม่สามารถแก้ไขข้อมูลได้

# 2.การเข้าถึงข้อมูล

'''ใช้แค่ [] เท่านั้น ใน tup[2]'''
print(tup[2]) #ห้ามใช้ () ใน tup[2] เช่น tup(2) => Xห้ามX
#ใช้เหมือน List

# 3.การเข้าถึงข้อมูลแบบกำหนดช่วงเวลา (Slice)

print(tup[0:3])
print(tup[1:])
print(tup[-1:-3])
print(tup[-4:])
#ใช้เหมือน List

# 4.การแก้ไขข้อมูล

#tup[0]="กรุงเทพ"#ไม่สามารถแก้ไขข้อมูลได้
#แต่ สิ่งนี้ทำได้
lis=list(tup)
lis="กรุงเทพ"
print("ก่อนแก้ไข =>",tup)
tup=tuple(lis)
print("หลังแก้ไข =>",tup)
#โดย แปลง Tuble เป็น List ก่อน 'จึงแก้ไขข้อมูลได้'
#แล้ว จึงแปลง List เป็น Tuble เหมือนเดิม เพือใช้งาน Tuble ต่อ

# 5.แสดงผลด้วย Loop

for item in tup:
    print("สมาชิก =",item)

# 6.ตรวจสอบข้อมูล

tup1=tuple((1,2,3,4,"kongruksiam","มะม่วง",True,3.99))
if "ทุเรียน" in tup1:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")

# 7.นับจำนวนสมาชิก (len)

#0-7 index
#1-8 len
print(len(tup1))

# 8.len() ทำงานร่วมกับ Loop for

for me in range(len(tup1)):
    print(tup1[me]) #tup[0] , tup[1] , .... , tup[7]

# 9.การสร้าง และ เพิ่มข้อมูล (Join)

# การสร้าง
# รูปแบบที่ 1
x=() #มีพื้นที่ให้ใส่สมาชิกเข้าไปเพิ่มได้
print(x)

# รูปแบบที่ 2
x=tuple()
print(x)

# รูปแบบที่ 3
x=("kongruksiam")   #str
y=(1)               #int
z=("kongruksiam",)  #tuple เติม"," ให้มีพื้นที่ใส่สมาชิกเข้าไปเพิ่มได้
print(type(x))
print(type(y))
print(type(z))

# การเพิ่มข้อมูล
name=("kongruksiam","jojo")
new=("nut",) # ห้ามใช้ new="nut" เฉย เพราะเป็น str

name=name+new # หรือ ใช้ name=name+(new,) ตอนที่ด้านบนใช้ new="nut" '''แนะนำแก้ไขตรงนี้ดีกว่าด้านบน'''
# ลดรูปใช้ name+=new
print(name)

#หรือ

#ในกรณี สร้าง Group ใหม่ขึ้นมา โดยไม่กระทบต่อ tuple อื่น
allGroup=()
allGroup=name+new
print(allGroup)

# 10.ทำงานร่วมกับ list

city=["กรุงเทพ","อุบล","ชลบุรี"]

tup1+=tuple(city) #ลดรูป
print(tup1)

# 11.การลบข้อมูล del , การลบแบบ list

#การลบข้อมูล del
'''
del(tup)
print(tup)
'''

#การลบแบบ list
#แปลง tuple เป็น list แล้ว ใช้วิธี list ในการลบเอา
print("Before =>",tup1)
lis=list(tup1)
lis.remove("มะม่วง")
tup1=tuple(lis)
print("After =>",lis)

# 11.การค้นหา และ นับจำนวนสมาชิก (count)

tup2=(1,2,3,4,"kongruksiam","มะม่วง",True,3.99,4)

#นับจำนวนสมาชิก (count)
x=tup2.count(4)
print(x) # เจอเลข 4 มีอยู่ 2 ที่

# 12.การค้นหาสมาชิก (index)

x=tup2.index(4)
print(x) # เจอเลข 4 ที่ index = 3

# 13.การ sort ช้อมูล

tup3=(100,99,98,50,200,1,2,3,4,3.99,4) #ห้ามใช้ตัวหนังสือ

#เขียนแบบนี้ไม่ได้
'''
tup3.sort()
print(tup)
'''
#ต้องแปลง Tuple เป็น list ก่อน
print("Before =>",tup3)
lis=list(tup3)
lis.sort()
tup3=tuple(lis)
print(lis)
print("After =>",tup3)