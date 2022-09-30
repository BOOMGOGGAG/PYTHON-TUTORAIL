#break / continue

#break
i=1
while i<=10:
    print("รอบที่ = ",i)
    if(i==5):
        break #หลุดออกจาก Loop
    i+=1
else :
    print("จบ")

print("\n")

#continue
l=0
while l<=10:
    l+=1
    if(l%2 != 0):
        continue #ยังอยุูใน Loop แต่จะกระโดดข้ามตาม เงื่อนไขที่เรากำหนด
    print("รอบที่ = ",l)

for i in range(1,11):
    if(i%2 == 0):
        continue
    print(i)