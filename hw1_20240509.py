#題目:亂數產生5~100之間可被5整除的數 產生5個且不重複(請用5個變數去儲存)
import random

one=0
two=0
three=0
four=0
five=0
for i in range(5000): #產生多個亂數
    num = random.randrange(5,101,5) #產生亂數
    #print(num)
    if i==1: #判斷迴圈是否跑第一次
        one=num #第一次不與其他數重複
    else:
        if two == 0: 
            if one != num:
                two = num
        elif three == 0:
            if one != num and two != num :
                three = num
        elif four == 0:
            if one != num and two !=num and three != num :
                four = num
        elif five == 0:
            if one != num and two != num and three != num and four != num:
                five = num
                break
print("one:",one,"two:",two,"three:",three,"four:",four,"five:",five)

            
            


    
    
