"""
利用for迴圈計算1~100的奇數並印出奇數和
1~100 可被7整除的數加總
1-100列出同時可被5和15整除的數
"""

total=0
num=0
for i in range(1,101): #這是for迴圈
    if i%2==1 : #這是找出奇數值的判斷式
        print(i) #這是列出1~100之間的所有奇數
        total+=i #這是所有奇數加總
    print(total) #這是輸出奇數和
    if i%7==0 : #這是找出1~100可被7整除的判斷式
        print(i)
        nub+=i 
        print(total)
    if i%5==0 and i%15==0:
        print(i)
    print("奇數和:",total)
    print("可被7整除之和",num)
    