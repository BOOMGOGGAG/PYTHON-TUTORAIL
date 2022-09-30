'''
โครงสร้างควบคุม (Control Structure)
1.แบบลำดับ
2.แบบเลือก
3.แบบทำซํ้า
'''

'''
if boolean expression :
    statement

'''

age=int(input("ป้อนอายุของคุณ : "))

if age>=15:   #เงื่อนไขเป็นจริง
    print("คำนำหน้าเป็น นาย/นางสาว")
    print("จบโปรแกรมด้านใน if")


'''
if จริง:
    ทำอะไร
else :
    ทำอะไร
'''

if age>=15:
    print("วัยรุ่น")
elif age>=20:
    print("วัยผู้ใหญ่")
elif age>=30:
    print("วัยทำงาน")
else :
    print("วัยเด็ก")

print("จบโปรแกรม")
