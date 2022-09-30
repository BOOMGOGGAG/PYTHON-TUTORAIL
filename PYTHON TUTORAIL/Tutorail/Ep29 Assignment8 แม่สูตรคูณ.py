# แม่สูตรคูณ

# แสดงแม่สูตรคูณ 2,3,4,5......
    #2x1....2x12....,3x1....,3x12,....

# 2,3

for x in range(2,13):
    print("แม่ = ",x)
    for y in range(1,13):
        print(x,'x',y," = ",(x*y))

#อยากป้อนแม่สูตรคูณที่คูณกับ 1-12 โดยระบุเอง
start=int(input("ป้อนมแม่สูตรเริ่มต้น = "))
stop=int(input("ป้อนแม่สูตรสุดท้าย = "))

for x in range(start,stop+1):
    print("แม่ = ",x)
    for y in range(1,13):
        print(x,'x',y," = ",(x*y))
