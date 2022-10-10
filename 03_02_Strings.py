# String slice in Python
# #
import math
name = 'My name is Vipul Goswami'
print(name[0])
# M
print(name[1])
# y
print(name[0:7])
print(name[:7])
# My name
print(name[11:])
# Vipul Goswami

myList = [1,2,3,4,5]
print(myList[2:4])
# [3,4]

print(len(name))
# 24
print(len(myList))
# 5

# String Formatting
# #
myNumber = 'My number is ' + str(5)
print(myNumber)
# My number is 5
myNumber = f'My number is {5}'
print(myNumber)
# My number is 5
print(f'My number is {5} and twice that is {2*5}')
# My number is 5 and twice that is 10
print(f'Pi is : {math.pi:.2f}')
# Pi is : 3.14
myPi = 'Pi is : {}'.format(math.pi)
print(myPi)
# Pi is : 3.141592653589793

myString = '''
Here is a long bloakc of text 
with newline 
'''
print(myString)
# Here is a long bloakc of text 
# with newline 