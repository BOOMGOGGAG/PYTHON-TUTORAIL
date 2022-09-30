#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
#BMI = นํ้าหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

#input
weight=int(input("ป้อนนํ้าหนักของ (kg) : "))
high=int(input("ป้อนส่วนสูงของคุณ (cm) : "))

#process
#cm => m
high=high/100#high/=100

#calculate bmi
bmi=weight/(high*high)#high**2

#output
print("BMI = ",bmi)#print("BMI = ",weight/(high*high))