#แปลงอุณหภูมิ
temp = input("ป้อนอุณหภูมิ (องศา) : ") #45c

degree=int(temp[:-1]) #45
unit=temp[-1].upper() #C

print(degree,"=",unit)
if unit=="C":
    #แปลงเป็นฟาเรนไฮน์
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮน์"
if unit=="F":
    #แปลงเป็นเซลเซียล
    result=(degree-32)*5/9
    unit_result="เซลเซียล"

print("แปลงตัวเลข = ",temp,"  เป็น ",unit_result," = ",result,"F")