# ค้นหาตัวเลขมากสุด / น้อยสุด

max,min = 0,999

#ถ้ามีตัวเลขที่น้อยกว่า 999 ก็จะนำตัวนั้นมาแทนที่ เช่น 10<999 min จะตอบ 10
while True :
    number=int(input("ป้อนตัวเลขของคุณ : "))
    #กระโดดออกจาก LOOP 
    if number<0 :
        break
    if number>max :
        max=number
    if number<min :
        min=number  

print("ค่าสูงสุด = ", max)
print("ค่าต่ำสุด = ", min)