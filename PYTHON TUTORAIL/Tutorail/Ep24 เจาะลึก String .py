#1.การเข้าถึงตัวอักษรใน string
'''
ตัวอักษร ใช้ '...'(นิยมใช้วิธีนี้)
ข้อความยาวๆ ใช้ "..."
'''
from typing import Text


name="songkiatchai"# index นับตำแหน่ง ต้อง เริ้มต้นที่ 0

#ใช้ตัว [] ระบุตำแหน่งที่เราต้องการให้ปรากฏ
print(name[0]) # ตำแหน่งของ name(ด้านบน) ซึ่งเริ้มต้นที่ 0
print(name[0:3]) # ตัวหน้าถึงท้าย(ที่เรากำหนด)

_name="songkiatchai studio"
print(_name[0:14])# เว้นวรรค ก็นับเป็นอีก 1 ตัวแหน่งด้วย

Name="songkiatchai : 160"
print(Name[-3])# ถ้าต้องการแค่ ตัวท้าย ใช้เครื่องหมาย - ได้
print(Name[-3:])# ถ้าหลัง : ว่างเปล่า จะคิดเป็น ตัวหน้าถึงท้าย

#2.การใช้ len function (ระบุจำนวนตำแหน่ง)
animal="  kong  "
print(len(animal))

#3.ลบช่องว่างซ้าย-ขวา (strip)
animal=animal.strip()
print(animal)

#4.แปลง case ของ string
animal1="  KoNg  "

print(animal1.upper())#ทำให้เป็น ตัวพิมพ์ใหญ่ ทั้งหมด
print(animal1.lower())#ทำให้เป็น ตัวพิมพ์เล็ก ทั้งหมด
print(animal1.capitalize())#ทำให้ ตัวแรก พิมพ์ใหญ่

#5.การแทนที่
mama="songkiatchai เกรด 1 อยู่ชั้น ม.1 ซอย 1"

print(mama.replace("1","4"))#จะเปลี่ยน ทั้งหมด จาก 1 เป็น 4
print(mama.replace("1","4",2))#จะเปลี่ยน เฉพาะตัวเลขแรก ตามที่เรากำหนด(เลข 2 คือ ตำแหน่งที่ไม่ต้องการให้เปลี่ยนจากซ้าย-ขวา)

#6.เช็คคำได้ว่ามีหรือไม่ โดย
meme="ไปซื้อข้าวและน้ำดื่มที่ตลาด"

x = "ข้าว" in meme#ใส่คำที่ต้องการลงใน "..." เช่น แทนคำว่าข้าว
y = "ข้าว" not in meme#ใส่ not ข้างหน้า in meme ได้
print(x)

if x:
    meme=meme.replace("ข้าว","ไข่")

print(meme)

#7.การต่อ String (Concatinate) +
fname="kong"
lname="ruksiam"
age="80"
salary=500.98755

fullname=fname+lname+age
print(fullname+"555")
print("ชื่อต้น :"+fname+"นามสกุล :"+lname+"\tอายุ :"+age)

#8.การจัดรูปแบบการแสดงผล format + {}
text="ชื่อต้น : {0}\tนามสกุล : {1}\t อายุ : {2}\tอาชีพ : {3}\tเงินเดือน : {4:.2f}"#.2f แสดงทศนิยมแค่ 2 ตำแหน่ง
print(text.format(fname,lname,age,"โปรแกรมเมอร์",salary))#สามารถใช้ตัวเลขระบุตำแหน่งได้ในคำสั่ง format เช่น 0 คือ fname และ 1 คือ lname และ age และ 3 คือ "โปรแกรมเมอร์"

#9.นับจำนวนคำในประโยค (count)
fruit="ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด แวะไปสวนทุเรียนด้วย"

print(fruit.count("ทุเรียน"))

#10.เช็คคำขึ้นต้น / เช็คคำลงท้าย

#เช็คคำขึ้นต้น
name="นายกอไก่ ใจดี"

if name.startswith("นาย"):
    print("เป็นเพศชาย")
else :
    print("เป็นบุคคลอื่น")

#เช็คคำลงท้าย
NaMe="1150"

if name.endswith("0"):
    print("ถูกหวย")
else :
    print("ไม่ถูกหวย")
