# Frozen set
# ไม่สามารถ "เพิ่ม" หรือ "ลบข้อมูลออก" ได้
fruit=frozenset(["มะม่วง","มะยม","มะนาว"])
fruit.add("ทุเรียน")
fruit.discard("มะยม")
print(fruit)
# แต่ "แสดงข้อมูล" ในรูปแบบต่างๆได้
for item in fruit:
    print("ข้อมูล =>",item)