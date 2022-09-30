# สาเหตุที่เราต้องเขียน funtion
# มีคำสั่งของโครงสร้างที่ 'ซ้ำกัน' "หลายจุด"
a,b,c,d=10,23,40,50

if a%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if b%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if c%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

if d%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")

# มีคำสั่งที่ 'ซ้ำกัน' "หลายจุด"

# 1.การสร้างและเรียกฟังก์ชั่น

# ห้ามสร้าง Function *ซ้ำกัน*(ในกรณีไฟล์เดียวกันนะ)
'''
def ชื่อฟังก์ชั่น () :
    statement
'''

def sayhi():
    print("Hello Function")

def saythailand():
    print("สวัสดี")

def sayenglish():
    print("Hello / Hi")

def add():
    x=3+1
    print(x)

# โปรแกรมหลัก(การเรียกฟังก์ชั่น)
add()
saythailand()
sayenglish()

# 2.Global variable และ Local variable

# เช่น
# Local
def displaynumber():
    #statemant
    x=10
    print("Hello = ",x,"ใน")

# โปรแกรมหลัก(การเรียกฟังก์ชั่น)
x=20
displaynumber()
print("Hello = ",x,"นอก")#ต้องใช้คำสั่ง print(Global)

'''
global
x ทั้งหมด
'''

'''
logal
x ใน
'''
# Local
def displaynumber():
    #statemant
    y=50
    a=100
    print("Hello = ",a,"ใน")

# โปรแกรมหลัก(การเรียกฟังก์ชั่น)
displaynumber()

# Global ต้องใช้คำสั่ง print
a=200 #ถ้าไม่มี a=200
print("นอก = ",a) #คำสั่ง print จะใช้งานไม่ได้

# นาย x ดารา => x ทั่วประเทศรู้จัก (Global)
# นาย x หมู่บ้านแสนสุข => x ในหมุ่บ้าน (Local)

# 3.การส่งค่าเข้ามาในฟังก์ชั่น

def myData(name): 
    print("Hello",name)

myData("Jojo")
myData("NUT")
myData(5)

#กรณีใส่ตัวแปรใน () มากกว่า 1 ตัว เช่น name1,name2
def myData(name1,name2):
    print("ชื่อ =",name1,"นามสกุล =",name2)

fname="BOOM"
lname="GOGGAG"

# โปรแกรมหลัก(การเรียกฟังก์ชั่น)
myData("Jojo","BOOM")
myData("NUT","ลุงเริง")
myData(5,10)

myData(fname,lname)

# 4.Arbitrary Arguments

# Arguments => เป็นค่าที่ส่งเข้าไปใน function => fname , lname , age (ตอนที่เรียกใช้ฟังก์ชั่น)
# Paramiter => ค่าตัวแปรที่รับข้อมูลที่ส่งมาทำงาน (Arguments) => a , b , c

def myData(a,b,c):# Paramiter
    print("ชื่อ =",a,"นามสกุล =",b,"อายุ =",c)

# Arguments
fname = "MAMA"
lname = "NANA"
age=16
myData(fname,lname,age)

def addition(a,b):
    print(a+b)

x=5
y=9
addition(5,9)
addition(x,y)

# อาส่ง - พารับ คือ Arguments - Paramiter

# 5.ฟังก์ชั่นเลขคู่ - เลขคี่ Assignment

def searchNumber(number):
    if number %2 == 0:
        print("เลขคู่")
    else :
        print("เลขคี่")

a1,b1,c1,d1=10,23,40,50
searchNumber(a1)
searchNumber(b1)
searchNumber(c1)
searchNumber(d1)

# 6.Arbitrary Arguments (args)

def add(x,y,z):
    print(x+y+z)

#add(10,20) #run ไม่ได้
add(10,20,5)
#add(10) #run ไม่ได้

#OR

'''
def add(x,y):
    print(x+y)

def add(x,y,z):
    print(x+y+z)

add(10,20)
add(10,20,5)
'''
#ก็ run ไม่ได้ เพราะ*ฟังก์ชันซ้ำกันไม่ได้*
#นอกจาก
def add(x,y):
    print(x+y)

def sumthree(x,y,z):
    print(x+y+z)

add(10,20)
sumthree(10,20,5)
#ถึงจะทำงานได้

#OR

def add(x,y):
    print(x+y)

def sumthree(x,y,z):
    print(x+y+z)

def sumfour(x,y,z,a):
    print(x+y+z+a)

add(10,20)
sumthree(10,20,5)
sumfour(10,20,5,10)

#ก็ได้เหมือนกัน

'''****เข้าเรื่องเลย****''''''****เข้าเรื่องเลย****''''''****เข้าเรื่องเลย****''''''****เข้าเรื่องเลย****'''
#ส่งตัวฟังก์ชั่น ไม่จำกัดจำนวน
#ใช้ *agrs อธิบายง่ายๆ คือ ใช้เครื่องหมายดอกจันทร์(*) แล้วตามด้วยชื่อ
#เช่น *item,*me,*number,*hglask

#เช่น
def add(*agrs):
    print(agrs)

add()
add(10)
add(10,20)
add(10,20,0,49)
add(10,20,30,40,50,60)

#AND
def add(*agrss):
    print(agrss[0]+agrss[1])

add(10,20)
add(10,20,0,49)
add(10,20,30,40,50,60)

#OR
def add(*agrse):
    sum=0
    for item in agrse:
        sum+=item
    print(sum)

add(10,20)
add(10,20,0,49)
add(10,20,30,40,50,60)

#OR
def add(*agrs1):
    sum1=0
    for i in range(len(agrs1)):
        sum1+=agrs1[i]
    print(sum1)

add(10,20)
add(10,20,0,49)
add(10,20,30,40,50,60)

# 7.Keyword Argument

def displayData(fname1,lname1,city):
    print("ชื่อ = ",fname1)
    print("นามสกุล = ",lname1)
    print("จังหวัด= ",city)

displayData("boom","ruk","ชลบุรี")
displayData("jojo","yare yare","กรุงเทพ")
print("\n")

'''การใช้ Keyword Argument'''
'''เพื่อ ไม่ให้เกิดข้อผิดพลาด ในการเรียงลำดับ'''

#ใช้ Keyword Argument
displayData(city="ชลบุรี",fname1="boom",lname1="ruk")
displayData(lname1="หล่อมาก",city="พะเยา",fname1="สมชาย")
print("\n")

#ไม่ใช้ Keyword Argument
displayData("ชลบุรี","boom","ruk")

# 8.Default Parameter

#สาเหตุ
'''
ถ้าระบุแค่ 2 จะใช้งานไม่ได้ ตามเงื่อนไขด้านบน บรรทัดที่ 254-257
displayData(fname1="โจโจ้",lname1="หล่อมาก")
'''
# Default Parameter หมายถึง การกำหนดค่าเริ่มต้น ให้กับ Parameter

def displayData(fname1,lname1,city="กรุงเทพ"):
    print("ชื่อ = ",fname1)
    print("นามสกุล = ",lname1)
    print("จังหวัด= ",city)

displayData(fname1="โจโจ้",lname1="หล่อมาก")
displayData(fname1="โจโจ้",lname1="หล่อมาก",city="ชลบุรี")

'''ถ้าป้อนครบ จะเป็นไปตามที่เราป้อน เช่น ถ้าไม่ป้อน city จะบังเป็น "กรุงเทพ"
                                  แต่ถ้าป้อน city ว่า "ชลบุรี" ก็จะเป็น ชลบุรี 
บรรทัดที่ 283     
'''

# 9.List Parameter

def displayfruit(item1):
    for o in range(len(item1)):
        print("ผลไม้ชิ้นที่ ",o+1," = ",item1[o])
    
def displayVet(item1):
    for o in range(len(item1)):
        print("ผักชิ้นที่ ",o+1," = ",item1[o])

fruit=["มะม่วง","มะละกอ","ฝร่ง","มะพร้าว"]
vet=('ชะอม','ผัดกาด','คะน้า')

displayfruit(fruit)
displayfruit(vet)

# 10.ฟังก์ชั่นแบบคืนค่า

"""
1.ไม่มีการรับค่าและส่งค่า
def name():

2.มีการส่งค่าเข้าไปทำงาน
def name(a,b):

3.รับส่งค่าเข้าไปทำงาน และส่งออกมา
def name(a,b):
    return a+b

เช่น

def add(a,b):
    return a+b

print(add(10,20))
#หรือ
x=add(10,20)
print(x)

4.ไม่มีการรับค่าเข้ามา แค่ส่งค่าออกไป

เช่น
def showNumber():
    return 500

x=showNumber()
print("ตัวเลข =",x)
#หรือ
print(showNumber())

"""

#Example
def randomNumber(x):
    if x == '100':
        print("ถูกหวย")
        return 1000

    else :
        print("ไม่ถูกหวย")
        return 0

money=randomNumber("1000")
print("เงินรางวัล = ",money)

#สมมติว่ามี'หนี้'
money1=randomNumber("100")
x=300
result=money1-x
print("เงินรางวัล = ",money1)
print("เงินคงเหลือ = ",result)

#11.return

def randomNumber(x):
    if len(x)<3 :
        return # return แบบนี้ได้
    if x == '100':
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย")
        return 0

money1=randomNumber("2")
print("เงินรางวัล = ",money1) # ถ้าเป็นไปตามเงื่อนไข จะขึ้นว่า "None" (เงื่อนไข if len(x)<3 :)

#12.Arbitrary Arguments (kwargs)

#กำหนดชื่อได้แบบ ไม่จำกัด(ใส่ paramiter ได้ โดยที่เราไม่ได้กำหนดไว้ในตอนแรกได้)
#ใช้ **kwargs อธิบายง่ายๆ คือ ใช้เครื่องหมายดอกจันทร์(**) แล้วตามด้วยชื่อ

#เช่น
#แบบปกติ
def displayData1(fname2) :
    print(fname2)

displayData1(fname2="songkiatchai")
#displayData1(fname2="songkiatchai",lname1="wongthaidee") จะ run ไม่ได้

#เช่น
#**kwargs
def displayData2(**kwargs):
    print(kwargs)

displayData2(fname2="songkiatchai")
displayData2(fname2="songkiatchai",lname1="wongthaidee",city="กรุงเทพ")
displayData2(fname2="songkiatchai",lname1="wongthaidee",statue="โสด")
displayData2(fname2="songkiatchai",lname1="wongthaidee",age=16,city="กรุงเทพ",statue="โสด")
displayData2(fname2="songkiatchai",lname1="wongthaidee",age=16,city="กรุงเทพ",statue="โสด",job="prigrammer")

# 12.1 ความแตกต่างระหว่าง ages และ kwargs

'''
*ages => ค่าใน paramiter มีได้หลายค่า
**kwargs => ชชื่อ paramier มีได้หลายชื่อ
'''

# 13.ฟังก์ชั่นเรียกฟังก์ชั่น

#EXAMPLE 1
def equal(x,y,z):
    a=compareMax(x,y) # ค่ามากสุด = 20
    m=compareMax(a,z) # ค่ามากสุด = 20,30
    return m # return a => 20,,,return m => 30

'''
ลดรูป
def equal(x,y,z):
    return compareMax(comparemax(x,y), z)
'''

def compareMax(x,y):
    if x>y:
        return x
    else :
        return y


max=equal(10,20,30)
print("ค่ามากสุด =",max)

#EXAMPLE 2
def displayFood():
    print("หูฉลาม")

def displayCity():
    displayFood()
    print("สวัสดีกรุงเทพ")

'''
OR
def displayCity():
    print("สวัสดีกรุงเทพ")
    displayFood()
'''

displayCity() #ไม่มีการส่งค่า

# 14.Recursive Function

def a():
    print("A")
    b()

def b():
    print("B")

a()

#loop infinite => ใช้สำหรับ เช่น ป้ายไปที่หกระพริบ ไปมาไม่หยุด
'''
def a():
    print("A")
    a()

a()

หรือ

def addNumber(number):
    if number==5:
        return
    print(number+1) #0 ทำให้ต้อง +1
    number+=1 #1
    addNumber(number)

addNumber(5)
'''

"""
หาจุดวนซ้ำ
หาจุดออกจาก function (return)
ต้อง paramiter
"""

#1-5 โดยไม่ใช้ คำสั่ง loop

def summation(number):
    if number==1:
        return number
    else :
        return number+summation(number-1)

x=summation(5) # ? =5+4+3+2+1
print(x)

"""
5
5 + summation(4)
5 + 4 + summation(3)
5 + 4 + 3 + summation(2)
5 + 4 + 3 + 2 + summation(2-1)
5 + 4 + 3 + 2 + summation(1)
5 + 4 + 3 + 2 + 1
=15
"""

# 15.แฟกทอเรียล (Factorial)

'''
มาจากหลักสูตรทางคณิตศาสตร์ ว่า 
เช่น 5!=5x4x3x2x1 =120
นั่นเอง
'''

def Factorial(number):
    if number==1:
        return number
    else :
        return number * Factorial(number-1)

x=Factorial(5)
print(x)

"""
5!

5
5xFactorial(4)
5x4xFactorial(3)
5x4x3xFactorial(2)
5x4x3x2xFactorial(1)
5x4x3x2x1
"""

# 16.Fibonacci Number

#ดูรูปภาพ image 2
# 0,1,1,2,3,5,8,...
# f0=? , f1=?

def Fibonacci(number):
    if number<=1:
        # 2 ลำดับแรก
        return number
    else :
        # เลขลำดับถัดไป
        return Fibonacci(number-1)+Fibonacci(number-2)

for i in range(5): #0-4
    print(Fibonacci(i))#0,1,1,2,3

"""
ผลลัพท์
i=0
i=1
i=2
i=3
i=4

0,1,1,2,3

"""

# 17.Pass Function

# ใช้ในกรณี "คิดคำสั่งไม่ออก"
# "ถ้าคิดออก ก็มาใส่ที่หลังได้"

#กรณีคิดคำสั่งไม่ออก
def getname():
    pass

getname()

#หรือ
def getyou(name):
    if name =="Song":
        print("ยินดีด้วย")
    else :
        pass

getyou("Song")

"""
#กรณี คิดออกแล้ว
def getname(name):
    print("Hello ,",name)

getname("Songkiatchai")

"""

# 18.Anonymous function

# ใช้กรณี "คิดชื่อฟังชันก์ไม่ออก"

"""
วิธีใช้ ดังนี้
lambda atguments : expresstion
"""
def getCity(name):
    print(name)

lambda name:print(name)

#หรือ
x=lambda name:name

print(x("songkiatchai"))

#หรือ
sum=lambda x,y : x+y

print(sum(5,10))

#หรือ(แถม)
def myPower(x):
    # x=ตัวเลข
    # a=เลขชี้กำลัง
    return lambda a : 5**a

y=myPower(5)
result=y(2) # 5**2

print(result)
