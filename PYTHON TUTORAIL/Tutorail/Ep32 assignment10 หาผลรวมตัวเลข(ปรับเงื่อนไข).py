#สามารถป้อนตัวเลขไม่จำกัด ถ้าไม่เป็นไปตามเงื่อนไขที่กำหนด
sum = 0
while sum<100: #ถ้ามี ผลรวม = 100 จะออกจาก Loop
    number=int(input("ป้อนตัวเลขของคุณ : "))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    print("ผลรวม = ",sum)

while True:
    number=int(input("ป้อนตัวเลขของคุณ : "))
    sum+=number
    if sum>100 :
        break #ถ้าใช้คำสั่ง break จะหลุดออกจาก Loop เลย โดยไม่แสดงคำสั่ง print("ผลรวม = ",sum) ด้านล่างนี้ 
    print("ผลรวม = ",sum)