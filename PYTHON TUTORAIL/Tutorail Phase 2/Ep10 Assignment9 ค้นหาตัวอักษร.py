#การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message=["aa","aab","cba","bba","abb","cca"]
result=[]

#count สั่งว่าจะนับตัวไหน คำว่าอะไร
for item in message:
    result.append(item.count("a"))
print(result)
