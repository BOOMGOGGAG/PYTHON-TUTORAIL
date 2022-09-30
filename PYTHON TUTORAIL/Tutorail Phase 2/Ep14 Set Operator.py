#หลักการ ดู ใน image 2
# 1.union นำข้อมูลใน 2 ตัวแปรมารวมกัน

fruitA={"กล้วย","มะยม","มะนาว"}
fruitB={"สตอเบอรี่","กีวี่","มะม่วง"}

#union กรณีสร้างตัวแปรใหม่
allFruit=fruitA.union(fruitB)
print(allFruit)

#update กรณีไม่ต้องการสร้างตัวแปรใหม่ 
fruitA.update(fruitB)
print(fruitA)

#copy
fruitC=fruitA.copy()
print(fruitC)

# ตัวแปร
fruitD={"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitF={"แอปเปิ้ล","ทุเรียน","สตอเบอรี่","กีวี่","มะม่วง"}

fruitJ={"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitK={"แอปเปิ้ล","ทุเรียน","สตอเบอรี่","กีวี่","มะม่วง"}

# 2.difference กรณีอยากสร้างตัวแปรใหม่
fruitG=fruitD.difference(fruitF)
fruitH=fruitF.difference(fruitD)
print(fruitG)
print(fruitH)

# 3.intersection กรณีอยากสร้างตัวแปรใหม่
fruitI=fruitD.intersection(fruitF)
print(fruitI)

# 4.difference_update กรณีไม่ต้องการสร้างตัวแปรใหม่ 
fruitD.difference_update(fruitF)
print(fruitD)

# 5.intersection_update กรณีไม่ต้องการสร้างตัวแปรใหม่ 
fruitJ.intersection_update(fruitK)
print(fruitJ)

# 6.subset นำกลุ่ม set มาเปรียบเทียบกัน ว่า set ที่สร้างขึ้นมา อยู่ในกลุ่ม set หลัก หรือไม่
fish={"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา","ปลาฉลาม","ปลาตะเพียน"}

# ข้อมูลสามชิกในตัวแปร x อยู่ในข้อมูล fish(set หลัก)**ทั้ง 2 ตัวไหม** (set ย่อยนี้ เป็นส่วนหนึ่ง ของ set หลัก ไหม)
x={"ปลาหมอ","ปลาซิว"}
print(x.issubset(fish))

y={"ปลาดุก","ปลาซิว"}
print(y.issubset(fish))

z={"ปลาดุก","ปลาฉลาม"}
print(z.issubset(fish))

# 7.superset ตรวจดูว่า มีสมาชิก fish อยู่ใน x **ทั้ง 2 ตัวไหม** (set หลักนี้ เป็นส่วนหนึ่ง ของ set ย่อย ไหม)
print(fish.issuperset(x))
print(fish.issuperset(y))
print(fish.issuperset(z))

# min / max
number={3,4,5,100,80,1000,500,300,-100,-8,150}

print(min(number))
print(max(number))