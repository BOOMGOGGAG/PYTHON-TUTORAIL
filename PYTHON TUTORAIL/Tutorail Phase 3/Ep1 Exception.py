#Exception หมายถึง "ข้อผิดพลาด"ต่างๆ ซึ่งข้อผิดพลาดนั่น(อาจจะ)เกิดจาก"คนที่ input "อะไรแปลกๆ

# 1.รู้จักกับ Exception

number1=int(input("ป้อนตัวเลข 1 :"))
number2=int(input("ป้อนตัวเลข 2 :"))
sum=number1+number2
print(sum)

"""
RUN!!!

ป้อนตัวเลข 1 : 1
ป้อนตัวเลข 2 : ก

ทำให้เกิดข้อผิดพลาด
สิ่งนี้จะเรียกว่า "Exception"
"""

# 2.Try...Except

"""
try :
    คำสั่ง RUN โปรแกรมปกติ
except :
    คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
"""
try :
    number1=int(input("ป้อนตัวเลข 1 :"))
    number2=int(input("ป้อนตัวเลข 2 :"))
    result=number1/number2
    print(result)
except :
    print("โปรแกรมมีข้อผิดพลาด")

# 3.จัดการ Exception หลายเหตุการณ์

#ValueError => ค่าผิดพลาด
#ZeroDisvisiomError => ข้อผิดพลาดที่เกี่ยวกับ เลข 0

try :
    number1=int(input("ป้อนตัวเลข 1 :"))
    number2=int(input("ป้อนตัวเลข 2 :"))
    result=number1/number2
    print(result)
except ValueError:
    print("ต้องป้อนตัวเลขเท่านั้นถึงจะหารได้")
except ZeroDivisionError:
    print("ห้ามหารด้วยเลขศูนย์นะครับ")

try :
    score=100+"50"
    print(score)
except TypeError:
    print("ชนิดข้อมูลไม่ตรงกัน")

# 4.ลดรูป Exception

# คำสั่งใน except Exception คือ คลังข้อมูลของข้อผิดพลาดทั้งหมดที่เกิดขึ้น
try :
    number1=int(input("ป้อนตัวเลข 1 :"))
    number2=int(input("ป้อนตัวเลข 2 :"))
    result=number1/number2
    print(result)
except Exception as e: #(as e คือ ให้ตั้งชื่อ Exception ว่า e)
    print(e)

# 5.Try...Exception..Else

# else คือ จะทำงาน ก็ต่อเมื่อ ไม่พบปัญหาในโปรแกรม
try :
    number1=int(input("ป้อนตัวเลข 1 :"))
    number2=int(input("ป้อนตัวเลข 2 :"))
    result=number1/number2
    print(result)
    print("โอนเงิน")
except Exception as e: #(as e คือ ให้ตั้งชื่อ Exception ว่า e)
    print(e)
else : 
    print("โอนเงินสำเร็จ")

# 6.Finally

# finally จะทำงานตลอด แม้ว่าจะมีข้อผิดพลาดเกิดขึ้น (ใช้สำหรับชุดคำสั่งที่ต้องทำงานอยู่ตลอดเวลา)
try :
    number1=int(input("ป้อนตัวเลข 1 :"))
    number2=int(input("ป้อนตัวเลข 2 :"))
    result=number1/number2
    print(result)
except Exception as e: #(as e คือ ให้ตั้งชื่อ Exception ว่า e)
    print(e)
finally :
    print("ทำงานต่อไป....")

# 7.Try..Except ทำงานร่วมกับ While

while True:
    try :
        number1=int(input("ป้อนตัวเลข 1 :"))
        number2=int(input("ป้อนตัวเลข 2 :"))
        if number1 == 0 and number2 == None :
            break
        result=number1/number2
        print(result)
    except ValueError:
            print("ต้องป้อนตัวเลขเท่านั้นถึงจะหารได้")
    except ZeroDivisionError:
            print("ห้ามหารด้วยเลขศูนย์นะครับ")
    finally :
        print("ทำงานต่อไป....")

# 8.สร้าง Exception ด้วย Raise

# raise คือ ถ้าเป็นไปตามเงื่อนไขหรือมีการใช้ raise ก็จะกระโดดข้ามจากฟังก์ชั่นหนึ่งไปอีกฟังก์ชั่นหนึ่ง เช่น จาก try ไป except เป็นต้น
while True:
    try :
        name=input("ป้อนชื่อผู้ใช้โปรแกรม :")
        if name == "ก้อง":
            raise Exception("มีชื่อในระบบแล้วนะครับ")
        number1=int(input("ป้อนตัวเลข 1 :"))
        number2=int(input("ป้อนตัวเลข 2 :"))
        if number1 == 0 and number2 == None :
            break
        if number1<0 or number2<0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้นะครับ")
        result=number1/number2
        print(result)
    except Exception as e: #(as e คือ ให้ตั้งชื่อ Exception ว่า e)
        print(e)
