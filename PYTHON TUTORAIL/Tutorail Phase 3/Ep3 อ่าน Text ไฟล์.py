"""
รูปแบบ
open("ชื่อไฟล์","โหมด","เข้ารหัส")
"""
"""
โหมด r คือ read(อ่าน)
โหมด w คือ write(เขียน)
โหมด a คือ append(การต่อข้อความเข้าไปที่ไฟล์ text)
โหมด x คือ การ create ไฟล์ขึ้นมาใหม่
โหมด t คือ text file
โหมด b คือ binary file
"""
fr=open("student(ใช้ใน Phase 3).txt","r",encoding="utf-8")
print(fr.read())

#หรือ

try:
    fr=open("student(ใช้ใน Phase 3).txt","r",encoding="utf-8")
    print(fr.read())
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")