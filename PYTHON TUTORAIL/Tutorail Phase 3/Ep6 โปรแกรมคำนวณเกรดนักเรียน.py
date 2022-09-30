#ป้อนคะแนน
try:
    fw=open("document.txt","a",encoding="utf-8")
    while True :
        studentid=input("ป้อนรหัสนักเรียน :")
        if studentid == "exit" :
            break
        score=input("ป้อนคะแนนสอบ :")
        fw.writelines(studentid+"\t"+score+"\n")
    fw.close()
except Exception as e:
    print(e)

#คำนวณเกรด
try:
    fr=open("document.txt","r",encoding="utf-8")
    fw=open("Grade.txt","a",encoding="utf-8")
    grade=None
    for line in fr.readlines():
        score=line[-4:].strip() #.strip() คือ การลบช่องว่างออก
        studentid=line[:-4].strip()
        #print("รหัส = ",studntid,"คะแนน",score)
        score=int(score)
        if score>=80:
            grade="A"
        elif score>=70 and score<80:
            grade="B"
        elif score>=50 and score<=69:
            grade="C"
        else :
            grade="F"
        #print("รหัส = ",studentid,"คะแนน = ",score,"เกรด = ",grade)
        fw.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
    fw.close()
    fr.close()
    
except Exception as e:
    print(e)