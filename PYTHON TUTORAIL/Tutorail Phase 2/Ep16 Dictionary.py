#list , tuple
lis=["สีแดง","สีเหลือง","สีเขียว"]
tup=("สีแดง","สีเหลือง","สีเขียว")

#dictionary => key (การเข้าถึงข้อมูล), value (ค่าของข้อมูล)
# หน้าที่ : ค้นหาข้อมูลในตัวแปร
#list , tuple => index , value

# 1.การสร้าง dict และ การเข้าถึง

''' ชื่่อตัวแปร = {key:value,key:value,key:value} '''
# EXAPLE
colors1={"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป้า",True:"โสด",False:"มีผัวแล้วอีดอก"}
colors={"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป้า",True:"โสด",False:"มีผัวแล้วอีดอก"}
print(colors["red"])# ใส่ key
# OR
print(colors.get("red")) 
print(colors[False])

city={"bangkok":"กรุงเทพ"}
print(city["bangkok"])

animal={"ไก่":"chicken","แมว":"cat","dog":"น้องหมา"}
print(animal["ไก่"])

student={"ก้อง":40,"โจ้":50,"โค้ช":100}
print(student["ก้อง"])

room={300:"นาย A",301:"นาย B",302:"นาย C"}
print(room[300])

# รูปแบบ constructor
pet=dict(cat="แมว",dog="น้องหมา",duck="น้องเป็ด")
print(pet["cat"])

# 2.การแก้ไขข้อมูล

colors[100]="ป่าสวน"
print(colors)
colors.update({"red":"สีชมพู"}) #ถ้าฟังก์ชันซ้ำกันจะ แทนที่ ข้อมูลนั้น

# 3.การเพิ่มข้อมูล

colors.update({"blue":"สีน้ำเงิน","orange":"สีส้ม"})
print(colors)

# 4.Loop

# แสดง key
for item in colors:
    print(item)
print("\n")

# แสดงเฉพาะ key
for item in colors.keys():
    print(item)
print("\n")

# แสดงเฉพาะ value
for iten in colors.values(): 
    print(iten)
print("\n")

for k,v in colors.items():
    print(k)# แสดงเฉพาะ key
    print(v)# แสดงเฉพาะ value

# 5.การลบข้อมูล

print(colors)
colors.pop("red")
print(colors)

# นำข้อมูล ล่าสุด ออก
colors.popitem()
print(colors)

# ลบข้อมูลในสมาชิกออก
colors.clear
print(colors)

# ลบตัวแปรออก
del colors
#print(colors)

# 6.การคัดลอก copy

x=colors1.copy()
print(x)

# 7.นำข้อมูลมาซ้อนกัน

market={
    "ร้านป้าพร":{
        "name":"ป้าพร",
        "menu":["กะเพราไก่","ก๋วยเตี๋ยว"],
        "zome":'ตะวันออก'
    },
    "ร้านลุงป้อม":{
        "name":"น้าจ็อบ",
        "menu":["มะม่วง","ทุเรียน"],
        "zome":'ทางเข้าตลาด'
    },
    "ร้านน้าใจ":{
        "name":"น้าใจ",
        "menu":["นมปั่น","ชาเย็น"],
        "zome":'ช้าง 7-11'
    }
}

print(market["ร้านป้าพร"]["menu"])
print("ก๋วยเตี๋ยว" in market["ร้านป้าพร"]["menu"])

# 8.การค้นหาข้อมูล

if "ก๋วยเตี๋ยว" in market["ร้านป้าพร"]["menu"]:
    print('เป็น')
else :
    print("ไม่เป็น")