# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง (m)
# input / convert to interger
weight = int(input("ป้อนน้ำหนักของคุณ (kg) :"))
height = int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100

bmi = weight/(height**2)

result="ไม่ทราบค่าที่ชัดเจน"
if bmi<18.0 :
    result="ต่ำกว่าเกณฑ์"

elif bmi >=18.5 and bmi<=22.9 :
    result="สมส่วน"

elif bmi >=23.0 and bmi<=24.9 :
    result="น้ำหนักเกิน"

elif bmi >=25.0 and bmi<=29.9 :
    result="โรคอ้วน ระดับที่ 1"

elif bmi >30.0 :
    result="โรคอ้วนระดับอันตราย"

print("ค่า bmi = ", bmi ,"ทำนายว่า =",result)

'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วน ระดับที่ 1
>30 = โรคอ้วนระดับอันตราย

'''