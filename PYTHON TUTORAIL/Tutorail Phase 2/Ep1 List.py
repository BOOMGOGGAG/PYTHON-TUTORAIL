# เขียนแบบ primitive

a=1
a1=2
a2=3
a3=4
a4=5
a5=6
a6=7

# 1.non primitive : list

number=[] # list ว่าง
number=[1,2,3,4,5,6] # list มีสมาชิก 1,2,3,4,5,6 (สามารถระบุได้ทั้งตัวเลขและตัวอักษร)
name=["นาย A","นาย B","นาย C"] #list name มีสมาชิก นาย A,นาย B,นาย C (สามารถระบุได้ทั้งตัวเลขและตัวอักษร)
all=[10,"นายไข่",True,3.14,-10]

# construtor (เขียนอีกรูปแบบ)
name=list(["นาย A","นาย B","นาย C"])

# แสดงผล
print(name)
print(all)
print(number)

# 2.เข้าถึงข้อมูลของ List

'''ดูรูป image'''
# (ซ้ายไปขวา)
print(number[2]+number[0]) # กรณีอยากได้เลข 4 หรือ print(number[3]) ก็ได้
'''ถ้า print(name[5]) จะขึ้นว่า IndexError: list index out of range เพราะไม่มี '''
# (ขวาไปซ้าย)
print(all[-3])

# ระบุว่าส่าจะ เริ่มต้น-จบ ตรงไหน
# (ซ้ายไปขวา)
print(all[1:4])
# (ขวาไปซ้าย)
print(all[-4:-1]) 

# 3.กรณีไม่ระบุ จุดเริ่มต้นหรือตัวสุดท้าย

#กรณีไม่ระบุ จุดเริ่มต้น
print(all[2:]) # จะระบุตัวท้าย
#กรณีไม่ระบุ ตัวสุดท้าย
print(all[:-1]) # จะเป็นการ ตัดตัวท้ายทิ้ง แล้ว นำตัวที่เหลือมาใส่แทน ตามลำดับปกติ คือ จากซ้ายไปขวา

# 4.การแก้ไขข้อมูล

# ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"

print("ก่อนแก้ไข => ",number)
number[2]=9
number[-1]="นายไข่"
print("หลังแก้ไข => ",number)

# 5.แสดงผลด้วย loop

for item in number :
    print(item)

# 6.ตรวจสอบช้อมูล => ใช้สำหรับตรวจสอบคนได้ หรือ ข้อมูลได้
fruit=["มะม่วง","มะนาว","มะยม","มะละกอ"]

if 9 in number :
    print("เป็น")
else :
    print("ไม่เป็น")

if "มะยม" in fruit :
    print("เป็น")
else :
    print("ไม่เป็น")

# 7.นับจำนวนสมาชิก len

print(len(number))
print(len(fruit))

# 8.len() ทำงานร่วมกับ loop,for ได้

for i in range(len(fruit)):
    print(fruit[i])

for item in fruit:
    print(item)

# 9.การเพิ่มข้อมูล => append , insert

#append() คือ การนำเอาข้อมูลมาต่อท้าย
print("ก่อนเพิ่ม =>",fruit)

fruit.append("มะปราง") 
fruit.append("แตงโม")
print("หลังเพิ่ม =>",fruit)

#insert (index,สมาชิกใหม่) คือ การนำเอาข้อมูลไปแทรก
print("ก่อนแทรก =>",fruit)
fruit.insert(1,"ทุเรียน")
print("หลังแทรก =>",fruit)

# 10.การลบข้อมูล => remove , pop , del , clear

# remove คือ ลบ โดยการ'ระบุชื่อในตัวแปร'
fruit.remove("มะยม")
print("remove =>",fruit)

# pop ลบ'ตัวล่าสุด'ออก และ สามารถลบได้เรื่อยๆ จนกว่าจะหมด
fruit.pop()
fruit.pop()
print("pop =>",fruit)

# del คือ ลบ โดยการใช้ index และสามารถ ลบ'ตัวแปรทั้งหมด'ได้ด้วย
# del  คือ ลบ โดยการใช้ index
del fruit[1]
print("del =>",fruit)
# และสามารถ ลบ'ตัวแปรทิ้งไปเลย'ได้ด้วย
# del fruit
# print(fruit)

# clear คือ การ'ล้างข้อมูลในตัวแปรออกหมด' เป็น 'ตัวแปรเปล่า'
print(fruit)

# 11.การคัดลอกข้อมูล copy

# copy คือ การคัดลอก'ข้อมูล'จาก'ตัวแปรหนึง'สู่'อีกตัวแปรหนึ่่ง'
print()
y=[]
print(y)
y=fruit.copy()
print(y) 

# 12.การรวมข้อมูล (+)
allGroup=number+fruit
print(allGroup)

# 13.แสดงจำนวนสมาชิก count
# การหาข้อมูลในตัวแปร(list) ว่ามี'ซ้ำกัน'กี่ที่
Number=[1,2,3,4,5,5,5,6,7,8,9]
z=Number.count(5) #integer
print(z)

# 14.extand
# คือ การนำ list 2 ตัว มารวมกัน กลายเป็น list ก้อนใหม่
''' โดย'ไม่ต้องสร้าง list อีกอันหนึ่งใหม่' '''

number.extend(fruit)
print(number)
