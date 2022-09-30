#Assignment หาค่ามากสุด / ค่าต่ำสุด / ผลรวมตัวเลข
number1=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0:
        break
    number1.append(x)

print(number1)
print("ค่าน้อยสุด คือ",min(number1))
print("ค่ามากสุด คือ",max(number1))
print("ผลรวม คือ",sum(number1))
