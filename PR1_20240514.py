# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
隨機產生1~49之間的正整數
1-1 黑名單:不可被新增進去 10 15 39
1-2 請使用RANDOM來自動新增六個數字
1-3 白名單:一定要有17 41
"""
import random
number = list()

while True:
    num = random.randrange(1,50)
    number.append(num)
    print("一開始的數",number) 
    #我要判斷list內有沒有10 
    if number.count(10) == 1 :
        number.remove(10) #被移除的數
        print("刪除結果",number)
    if number.count(15) == 1 :
        number.remove(15) #被移除的數
        print("刪除結果",number)
    if number.count(39) == 1 :
        number.remove(39) #被移除的數
        print("刪除結果",number)
    if len(number) == 6 :
        break
print("最後",number)



