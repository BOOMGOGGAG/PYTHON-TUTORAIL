#Type Coversion
x = 10
y = 3.14
z = "20"

# "20" => 20

#บวกเลข
result = str(x)+z
float(z)
result = x+y # 10+3.14 = 13.14
result = str(x)+z# "10" + "20" => result

# string => int
# int => string

print(result)
print(type(result))

# int => float

print(float(z))
print(str(y))
print(float(x))

# float => int
print(int(y))

z=float(z)
z=z+50

print(z)