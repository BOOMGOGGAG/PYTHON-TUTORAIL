#https://www.mathsisfun.com/games/towerofhanoi.html
#ดู image 2
"""
n=จำนวนจาน
เสา => A,B,C

มีจานจำนวน 3 จาน
ืn=1
n=2(n-1)
n=3(ใหญ่สุด)
"""

"""
A=> 3 => C => ใหญ่ => เล็ก

A => ล ก ญ
A (ล ก) => B
A ญ => C

C => ล ก ญ
"""

# def hanoi(จำนวนจาน,จุดย่อย,จุดพัก,จุดไป)
def hanoi(n,a,b,c):
    # a=>c
    if(n==0):
        return
    hanoi(n-1, a, c, b) #ย้่าย a (ล,ก) -> b | c จุดพัก (ย้าย,พักc,ไปb)
    print("จานที่ = ",n,"จาก = ",a,"ไป = ",c)
    hanoi(n-1, b, a, c)

hanoi(3,"A","B","C")