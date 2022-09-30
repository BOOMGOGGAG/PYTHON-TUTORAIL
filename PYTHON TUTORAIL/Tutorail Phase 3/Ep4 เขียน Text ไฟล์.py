try:
    fw=open("Score(ใช้ใน Phase 3).txt","w",encoding="utf-8")
    fw.writelines("Hello World\n")
    fw.writelines("สวัสดีชาวโลก")
    fw.close()
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")

#อ่านไฟล์
fr=open("Score(ใช้ใน Phase 3).txt","r",encoding="utf-8")
print(fr.read())
fr.close()

#หรือ
try:
    fr=open("Score(ใช้ใน Phase 3).txt","r",encoding="utf-8")
    line=fr.readlines()
    for x in line:
        print("=>",x)

    fr.close()
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")

#เขียนต่อ(แต่ต้องใช้โหมด a)
try:
    fw=open("Score(ใช้ใน Phase 3).txt","a",encoding="utf-8")
    fw.writelines("\nสวัสดีวันสงกรานต์")
    fw.close()
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")

#เขียนทับ(เมื่อใช้โหมด w)
# try:
#     fw=open("Score(ใช้ใน Phase 3).txt","w",encoding="utf-8")
#     fw.writelines("สวัสดีวันสงกรานต์")
#     fw.close()
# except FileNotFoundError:
#     print("หาไฟล์ไม่เจอจ้า")

#EXAMPLE another one
try:
    fw=open("Score(ใช้ใน Phase 3).txt","a",encoding="utf-8")
    for i in range(5):
        name=input("ป้อนข้อความที่ต้องการ : ")
        fw.writelines(name+"\n")
    fw.close()
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")