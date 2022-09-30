#Loop ซ้อน Loop

i=1 # จำนวนรอบ

#while loop
while i<=3 : # หลัง
    j=1 # ตัวนับ(ตำแหน่ง)
    while j<=5 : # ก่อน
        print("รอบที่ = ",i,"ตำแหน่ง = ", j)
        j+=1
    i+=1

#for loop
for i in range(1,4):
    print("รอบที่ = ",i)
    for j in range(1,6):
        print("ตำแหน่ง = ", j)