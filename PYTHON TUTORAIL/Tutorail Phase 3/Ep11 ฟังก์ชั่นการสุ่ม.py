import random

x1=random.random() #0.0 - 1.0
print(x1,"\n")

for i in range(10):
    x=random.random() #0.0 - 1.0
    print(x)

for i in range(10):
    x=random.uniform(5,10) # 5 <= x <10 หรือ 5-9
    print(x)

"""
รูปแบบ คือ
random.randrange(start,stop,step)
"""
for i in range(15):
    x=random.randrange(-5,10,2) # -5 จนถึง 9 และกระโดดข้ามทีละ 2
    print(x)

for i in range(15):
    x=random.randint(1,5) # สุ่ม 1-5
    print(x)

items=[1,2,3,4,5,"A","B","C"] #list
for i in range(15):
    x=random.choice(items) # .choice() หยิบใช้งาน
    print(x)

for i in range(15):
    random.shuffle(items) # .shuffle() สลับข้อมูลภายใน
    print(items)

#รูปแบบ 2
for i in range(15):
    x=random.choice([1,2,3,4,5,"A","B","C"]) 
    print(x)

#รูปแบบ 3
for i in range(15):
    x=random.choice("12345ABCD") #string
    print(x)