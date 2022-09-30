# For Loop

# for in range(start,stop,step) #กำหนดรอบ
summation=0
for i in range(3): #summation
    print("รอบที่ = ",i) # เริ่มต้นที่ 0
print("\n")

for i in range(3): #0,1,2 กำหนดรอบ
    print("รอบที่ = ",i+1)#เริ่มต้นที่ 1 โดยการใช้ "i+1"
print("\n")

for i in range(5,11): #(start,stop)เริ่มที่เท่าไร แล้วหยุดที่เลขเท่าไร
    summation+=i
    print("รอบที่ = ",i,"sum = ", summation)
print("\n")

for i in range(-10,-3,2): #(start,stop,step)เริ่มที่เท่าไร แล้วหยุดที่เลขเท่าไร โดย"บวก"กี่ตำแหน่ง
    print("รอบที่ = ",i)
print("\n")

for i in range(10,0,-2): #(start,stop,step)เริ่มที่เท่าไร แล้วหยุดที่เลขเท่าไร โดย"ลบ"กี่ตำแหน่ง
    print("รอบที่ = ",i)