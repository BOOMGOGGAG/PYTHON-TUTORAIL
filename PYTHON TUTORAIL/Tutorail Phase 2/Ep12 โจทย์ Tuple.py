# นำค่าใน tuple => ตัวแปร
tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
print(c)
d=a+c
print(d)

# สลับ Tuple
x=(50,60)
y=(88,99)
print("Before x =>",x)
print("Before y =>",y)
x,y=y,x
print("After x =>",x)
print("After y =>",y)

# tuple => string
character=('k','o','n','g')
name="".join(character)
print(name)

# reverse tuple
f=(100,20,30,15,10,5,500)
reversed(f)
print(f)

#OR อยากสร้างตัวแปรใหม่

x=(100,20,30,15,10,5,500)
y=reversed(x) # y=tuple(reversed(x))
print(tuple(y)) # print(y)

# string to tuple
i="songkiatchai"
h=tuple(reversed(i))
print(h)
