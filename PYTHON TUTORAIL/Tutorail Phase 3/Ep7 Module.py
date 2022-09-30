"""
Module คือ การรวบรวมกลุ่มคำสั่ง ที่แยกย่อยมาจากตัวโปรแกรมหลัก มาเขียนอีกไฟล์หนึ่ง
เพื่อทำให้โครงสร้างของ Program ขึ้นง่าย ในการแก้ไขข้อผิดพลาด
"""

# 1.สร้างโมดูล (Module)

'''
โปรแกรมหลัก
def addition(*args):
     total=0
     for i in range(len(args)):
         total+=args[i]
    print("ผลบวก =",total)

addition(5,10,20)
'''
#ฟังก์ชั่นด้านบนนี้อยู่ใน Ep7(2)MainProgram2.py

import Ep7CalculateService
import Ep7Weather
Ep7CalculateService.addition(5,10,20)
print(Ep7CalculateService.PI)

result=Ep7Weather.city["ชลบุรี"]
print(result)

Ep7Weather.getWeather()

Ep7CalculateService.power(5, 2)

# 2.ตั้งชื่อให้กับโมดูล (Module)

# ตั้งชื่อเพื่อจะได้ไม่ต้องพิมพ์ชื่อเต็ม แต่เป็นชื่อย่อๆ
"""
รูปแบบ คือ 
import ...(ชื่อเต็ม)... as ...(ชื่อใหม่)....
"""
# เช่น
import Ep7CalculateService as cal
cal.addition(5,10,20)
print(cal.PI)

# 3.From Module

# เรียกใช้ เฉพาะฟังก์ชั่นที่เราต้องการได้ ซึ่งไม่ใช่ทั้งหมดจากฟังกั่นนั้น
"""
รูปแบบ คือ
from ...(ชื่อฟังก์ชั่นที่ต้องการ(.py))... import ...(เรียกใช้ชื่อฟังก์ชั่นด้านใน)...
หรือ
from ...(ชื่อฟังก์ชั่นที่ต้องการ(.py))... import *
"""
# เช่น

# ถ้าใช้โดยทั่วไป
import Ep7CalculateService
Ep7CalculateService.addition(5,10,20)

# ถ้าใช้แบบ From Module
from Ep7CalculateService import addition
addition(10,5,20)
#หรือ
from Ep7CalculateService import *
from Ep7Weather import *

print(PI)
print(city)