import os
import msvcrt as m



member = [line.rstrip('\n') for line in open('ListMember.txt')]
age = [line.rstrip('\n') for line in open('MemberAge.txt')]
COLOR = 'A'

NAME = "員工名冊系統"
while(1):
        
        os.system('color '+COLOR)
        os.system('cls')  
        member = [line.rstrip('\n') for line in open('ListMember.txt')]
        age = [line.rstrip('\n') for line in open('MemberAge.txt')]
        print(NAME.center(70," "))
        print("請選擇功能:")
        print("1.查詢現有員工")        
        print("2.增加新員工")
        print("3.刪除員工")        
        print("如需要更多模式介紹請打help,謝謝\n")
        
        mode = input("請輸入模式 =>")        
        if mode == '1':
                x = 0
                #print("目前的員工有:")                
                #print(member)                
                #print('年齡:')
                #print(age)
                for item in member:                        
                        print('員工姓名:'+member[x])
                        print('年齡:'+age[x])
                        print('')
                        x = x+1                
        if mode == '2':		
                name = input("請輸入新員工姓名 =>")
                member.append(name)
                AGE = input("請輸入新員工年齡 =>")
                age.append(AGE)
                print("   ")                
                print("已加入"+name+"員工"+" "+"年齡:"+AGE)
                file = open('ListMember.txt', 'w', encoding = 'Big5')
                file.truncate() 
                for item in member:
                        file.write("%s\n" % item)
                file.close()
                fileAGE = open('MemberAge.txt', 'w', encoding = 'Big5')
                fileAGE.truncate()
                for item in age:
                        fileAGE.write("%s\n" % item)
                fileAGE.close()
        if mode == '3':
                x = 0
                print("員工名單及年齡:"+'\n')
                member = [line.rstrip('\n') for line in open('ListMember.txt')]
                age = [line.rstrip('\n') for line in open('MemberAge.txt')]
                for item in member:
                        
                        print('員工姓名:'+member[x])
                        print('年齡:'+age[x])
                        print('')
                        x = x+1
                RE = input("請輸入你想要刪除的員工姓名 =>")
                x = member.index(RE)
                AGE = age[x]
                member.remove(RE)
                age.pop(x)
                file = open('ListMember.txt', 'w', encoding = 'Big5')
                for item in member:
                        file.write("%s\n" % item)
                file.close()
                fileAGE = open('MemberAge.txt', 'w', encoding = 'Big5')
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
                file = open('ListMember.txt', 'w', encoding = 'Big5')
                for item in member:
                        file.write("%s\n" % item)
                print("員工資料已儲存")
                file.close()
        if mode == "clear":
                CO = input("確定要刪除所有員工的資料嗎?(Y表示確定)=>")
                if CO == 'Y':
                   file = open('ListMember.txt','w', encoding = 'Big5')
                   file.truncate()
                   file.close()
                   fileAGE= open('MemberAge.txt', 'w', encoding = 'Big5')
                   fileAGE.truncate()
                   fileAGE.close()
                print("已刪除所有員工的資料")
                
        if mode == "about":
                print("This software is made by Jay Lee in Taiwan.")
                print("WARNING!!!!!    This software is only for Windows, can't run at OS X or Linux.")
        if mode == "help":
                print("模式介紹:")
                print("save 為儲存資料到電腦裡")
                print("exit 為離開本程式")
                print("color 為更改字體顏色")
                print("clear 為清除所有員工的資料\n")                
        if mode == 'color':
                COLOR = input("請輸入DOS中的色彩代號(不加color)=>")               
                
        print("   ")        
        os.system('pause')
       
                
                      
              
                
                
                      
