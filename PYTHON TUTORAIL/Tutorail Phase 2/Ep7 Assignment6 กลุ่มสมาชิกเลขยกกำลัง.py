#หาค่าเลขยกกำลัง
number=[1,2,3,4,5,6,7]
number1=[1,2,3,4,5,6,7]
print(number)
#ทั่วไป
for i in range(len(number)):
    number[i]=number[i]*number[i] #หรือ number[i]=number[i]**2
print(number)

#ลดรูป
number1=[i*i for i in number1]
print(number1)
