#ตารางหมากฮอต

'''

x=สีน้ำตาล
o=สีขาว

xoxox
oxoxo
xoxox
oxoxo
xoxox

'''
number=int(input("ป้อนขนาด = "))

#เริ่มที่ x
for row in range(number):
    for column in range(number):
        if (row+column)%2 == 0 :
            print("x",end="")
        else :
            print("o",end="")
    print(" ")

print("\n")

#เริ่มต้นที่ o
for row in range(number):
    for column in range(number):
        print("x",end="") if (row+column)%2 == 0 else print("o",end="")
    print(" ")

'''

3 x 3
# row = 0 + column = 0
# row = 0 + 1
# row = 0 + 2

# row = 1 + column = 0
# row = 1 + 1
# row = 1 + 2

# row = 1 + column = 0
# row = 2 + 1
# row = 2 + 2

'''

'''

xox
oxo
xox

'''