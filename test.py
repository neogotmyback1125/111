"""
随机生成两个 10 以内的实数（精确到小数点后两位）并输出到屏幕，
要求用户输入它们的和，然后判断用户的输入值，然后输出 True/False。
"""

from asyncore import read
from random import random

a = round(random()*10,2)
b = round(random()*10,2)
#print("Please input sum for ",a," + ",b,", =")
'''
c = input()
ci = float (c)
if ci == a + b:
    print(True)
else:
    print(False)
'''
c = input("Please input sum for %.2f + %.2f =\n" % (a, b))
ci = float (c)
if ci == a + b:
    print(True)
else:
    print(False)
