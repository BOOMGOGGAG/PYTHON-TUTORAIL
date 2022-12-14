"""
จัดกลุ่มข้อมูลพื้นฐาน
List = [] , ข้อมูลต่างชนิดกัน => แก้ไขสมาชิกข้อมูล ได้ & ข้อมูลซ้ำกัน ได้ , ข้อมูลซ้ำกัน ได้  , ซ้าย - ขวา
Tuple = () , ข้อมูลต่างชนิดกัน => แก้ไขสมาชิกข้อมูล ไม่ได้ & ข้อมูลซ้ำกัน ได้ , ข้อมูลซ้ำกัน ได้ , ขวา - ซ้าย
Set = {}  , ข้อมูลต่างชนิดกัน => แก้ไขสมาชิกข้อมูล ได้ & ข้อมูลซ้ำกัน ไม่ได้ , ข้อมูลซ้ำกัน ได้ , ลำดับไม่แน่นอน(นิยาม index ไม่ได้)
"""

# 1.Set แบบปกติ (นิยาม index ไม่ได้) ใช้สำหรับกรองข้อมูลว่า 'ซ้ำกันไหม'
fruit={"มะม่วง","มะขาม","มะยม"}
'''
print(fruit[0])
'''

# 2.constructor
fish=set(["ปลาดุก","ปลาหมอ","ปลาดุก",50,50])
print(fish) # จะไม่แสดงตัวแปรซ้ำ
lis=["ปลาทู","ปลาตะเพียน"]

#OR เขียนอีกรูปแบบ

mic=set(lis)
print(mic)

# 3.เพิ่มข้อมูลสมาชิก(ได้ไม่จำกัด)
fruit.add("ทุเรียน")
fruit.add("สับปะรด")
fruit.add(999)
print(fruit)

# 4.เพิ่มข้อมูลสมาชิก('หลายตัว'ในคราวเดียว)
lis=["ตะไคร้","โหระพา","ชะอม"]
fruit.update(lis)
print(fruit)

#OR เขียนอีกรูปแบบ

fruit.update(["ตะไคร้","โหระพา","ชะอม"])
print(fruit)

# 5.Loop
for item in fruit:
    print("ข้อมูล =>",item)

#นับจำนวนสมาชิกใน set
print(len(fruit))

# 6.ตรวจสอยข้อมูล
if "มะเฟือง" in fruit:
    print("มี")
else:
    print("ไม่มี")

#OR อีกรูปแบบ

print("มะเฟือง" in fruit)

# 7.ลบข้อมูลสมาชิก
# remove (ถ้าตัวที่ต้องการลบ ไม่มี จะขึ้น error)
fruit.remove("ทุเรียน")
print(fruit)

# discard (ถ้าตัวที่ต้องการลบ ไม่มี จะไม่มีอะไรเกิดขึ้น)
fruit.discard("มะปราง")
print(fruit)

#clear ลบข้อมูลสมาชิกในตัวแปร 'ทั้งหมด' (แต่ยังมีตัวแปรอยู่)
fruit.clear() # ตัวแปรเปล่า
print(fruit)

#del ลบตัวแปรทิ้ง
del fruit
print(fruit)
