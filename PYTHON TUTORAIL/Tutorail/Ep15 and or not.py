#การ and or not
age=int(input("ป้อนอายุของคุณ : "))
#35
#and
if age>=15 and age <=20:
    print("วัยรุ่น")
elif age>=20 and age<=29:
    print("วัยหนุ่มสาว")
elif age>=30 and age<=39:
    print("วัยผู้ใหญ่")
elif age>=80:
    print("วัยชรา")
else :
    print("วัยเด็ก")

#15 - 20 => วัยรุ่น
#21 - 29 => วัยหนุ่มสาว
#30 - 39 => วัยผู้ใหญ่

#or
if age>=15 or age <=20:
    print("วัยรุ่น")
else :
    print("วัยเด็ก")
print("จบโปรแกรม")

#15 - 20 => วัยรุ่น

#not
if not age>=15 :
    print("วัยรุ่น")
else :
    print("วัยเด็ก")
print("จบโปรแกรม")