# Module Date / Time
import datetime

result=datetime.datetime.now() #ตั้งวัน/เวลาปัจจุบันมาใช้งาน
print(result) #แสดงทั้งหมด
print(result.year)  #แสดงเฉพาะปี
print(result.month) #แสดงเฉพาะเดือน

newdate=datetime.datetime(2020, 6, 20) # yyyy.month.day
print(newdate)

#รูปแบบแสดงผล แบบ day.month.yyyy
import datetime
print("เริ่มต้น",result)

# รูปแบบสั้น m/d/y 
print(result.strftime("%x \n"))  #"x ตัวพิมพ์เล็ก"
# รูปแบบสั้น เวลา time
print(result.strftime("%X \n"))  #"X ตัวพิมพ์ใหญ่"

# รูปแบบ คือ วัน(จันทร์-อาทิตย์),เดือน,วันที่,เวลา,ปี ตามลำดับ
print(result.strftime("%c \n"))

# เวลาอย่างเดียว(ชั่วโมง) เช่น 12:56:20 น. ผลลัพธืที่ได้ คือ 12
print(result.strftime("%H"))
# เวลาอย่างเดียว(นาที) เช่น 12:56:20 น. ผลลัพธืที่ได้ คือ 56
print(result.strftime("%M"))
# เวลาอย่างเดียว(วินาที)เช่น 12:56:20 น. ผลลัพธืที่ได้ คือ 20
print(result.strftime("%S"))
# หน่วยเวลา คือ AM,PM
print(result.strftime("%p \n"))

#EXAMPLE
print(result.strftime("%H:%M:%S %p \n"))

# 1-365 วัน
print(result.strftime("%j \n"))

# วัน(Sunday-Monday)
print(newdate.strftime("%a")) #แบบย่อ
print(newdate.strftime("%A")) #แบบเต็ม
print(result.strftime("%w \n")) # 0 คือ Sunday,1 คือ Monday,2 คือ Tueday...,6 คือ  Saturnday

# วันที่อย่างเดียว
print(result.strftime("%d"))
# เดือน วัน ปี ตามลำลับ
print(result.strftime("%D \n"))

# เดือน
print(result.strftime("%b")) #แบบย่อ
print(result.strftime("%B \n")) #แบบเต็ม

# ปี
print(result.strftime("%y")) #แบบย่อ
print(result.strftime("%Y \n")) #แบบเต็ม

#EXAMPLE2
print(result.strftime("วันที่ %d ประจำวันที่ %A เดือน %B ปี %y"))

# ว/ด/ป
print(result.strftime("%d"))