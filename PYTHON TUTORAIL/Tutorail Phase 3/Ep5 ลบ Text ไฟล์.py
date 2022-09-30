import os
# os หมายถึง การลบไฟล์ทิ้ง
try:
    if os.path.exists("Score(ใช้ใน Phase 3).txt"):
        os.remove("Score(ใช้ใน Phase 3).txt")
        print("ลบแล้วนะครับ")
    else :
        print("ไม่พบไฟล์นี้ครับผม")
except Exception as e:
    print(e)