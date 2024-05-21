# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#題目:亂數產生5~100之間可被5整除的數 產生5個且不重複，使用串列

import random
number = list()

while len(number) != 5 :
    n = random.randrange(5,101,5)
    if number.count(n) == 0 : #不重複
        number.append(n)
print(number)   