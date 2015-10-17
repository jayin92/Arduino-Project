import os
import msvcrt as m

member = [line.rstrip('\n') for line in open('ListMember.txt')]
age = [line.rstrip('\n') for line in open('MemberAge.txt')]
while(1):
        os.system('cls')  
        member = [line.rstrip('\n') for line in open('ListMember.txt')]
        age = [line.rstrip('\n') for line in open('MemberAge.txt')]
        print("                            瑞領公司員工名冊系統\n")
        print("請選擇功能:")
        print("1.查詢現有員工")        
        print("2.增加新員工")
        print("3.刪除員工")        
        print("如需要更多模式介紹請打help,謝謝\n")
        
        mode = input("請輸入模式 =>")        
        if mode == '1':
                print("目前的員工有:")                
                print(member)                
                print('年齡:')
                print(age)
        if mode == '2':		
                name = input("請輸入新員工姓名 =>")
                member.append(name)
                AGE = input("請輸入新員工年齡 =>")
                age.append(AGE)
                print("   ")                
                print("已加入"+name+"員工"+" "+"年齡:"+AGE)
                file = open('ListMember.txt', 'w', encoding = 'UTF-8')
                file.truncate() 
                for item in member:
                        file.write("%s\n" % item)
                file.close()
                fileAGE = open('MemberAge.txt', 'w', encoding = 'UTF-8')
                fileAGE.truncate()
                for item in age:
                        fileAGE.write("%s\n" % item)
                fileAGE.close()
        if mode == '3':
                print("員工名單及年齡:")
                member = [line.rstrip('\n') for line in open('ListMember.txt')]
                age = [line.rstrip('\n') for line in open('MemberAge.txt')]
                print(member)
                print(age)
                RE = input("請輸入你想要刪除的員工姓名 =>")
                x = member.index(RE)
                AGE = age[x]
                member.remove(RE)
                age.pop(x)
                file = open('ListMember.txt', 'w', encoding = 'UTF-8')
                for item in member:
                        file.write("%s\n" % item)
                file.close()
                fileAGE = open('MemberAge.txt', 'w', encoding = 'UTF-8')
                fileAGE.truncate()
                for item in age:
                        fileAGE.write("%s\n" % item)
                fileAGE.close()
                print(RE+"員工已刪除"+" "+"年齡"+AGE)                
        if mode == "exit":                
                Exit=input("你確定要離開嗎?(Y or N)")
                if Exit == 'Y':
                        exit()
                        """
                        for item in member:
                                file.write("%s\n" % item)
                                """ 
        if mode == "save":
                file = open('ListMember.txt', 'w', encoding = 'UTF-8')
                for item in member:
                        file.write("%s\n" % item)
                print("員工資料已儲存")
                file.close()
        if mode == "clear":
                CO = input("確定要刪除所有員工的資料嗎?(Y表示確定)=>")
                if CO == 'Y':
                   file = open('ListMember.txt','w', encoding = 'UTF-8')
                   file.truncate()
                   file.close()
                   flieAGE = open('MemberAge.txt', 'w', encoding = 'UTF-8')
                   fileAGE.truncate()
                   fileAGE.close()
                print("已刪除所有員工的資料")
                
        if mode == "about":
                print("This is made by Jay Li in May 28, 2015. I'm glad you download this stupid software")
        if mode == "help":
                print("模式介紹:")
                print("save 為儲存資料到電腦裡")
                print("exit 為離開本程式")
                print("clear 為清除所有員工的資料\n")                
                print("如何使用這個程式:")
                print("如果員工姓名為Jay,年齡為12,表示方法如下:")
                print("目前員工有:")
                print("['Jay']")
                print("年齡:")
                print("['12']")
        print("   ")        
        os.system('pause')
       
                
                      
              
                
                
                      
