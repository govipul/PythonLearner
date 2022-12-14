from decimal import Decimal, getcontext
# 👆 means import decimal from Decimal class and import the method getcontext
# #

print(20/4)
# 5.0

print(4 + 4.0)
# 8.0

print(4 * 4.0)
# 16.0

print(4 ** 4.0)
# 256.0

print(int(4 ** 4.0))
# 256

print(int(8.9999999)) # <-- here we are casting 8.9 to 8
# 8
# Python in-built classes all starts with small letters which breaks the conventions.
# like int, str, float
# ##

print(round(8.99999))
# 9

print(round(14/3, 2)) # <-- Round this till 2 digit
# 4.67

print(1.2 - 1.0) 
# 0.199999999999999
# 👆 its making use of approximation when storing the floats and hence we have the problem
# to solve this issue we have to make use of the function round.
# its is called 'floating point error'

print(round(1.2 - 1.0), 2)
# 0.2

print(int('100'))
# 100

print(int('100', 2)) # <-- In base 2 100 is 4
# 4 

print(int('1ab', 16)) # <-- in base 16 this is a  valiad number
# 427
#
# 👆 as we can see that in type cast the 1st variable is string and the reason is we can have 
# various number in base 16 or any other string in different format so its very simple to keep the first argument
# as String
# #

print(getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
# As float have 'floating point errror', python has comeup with the class called Decimal
# so now if we want to change the precision form 28 -> 4 we have do following steps 
# #

getcontext().prec = 4
output = Decimal(1)/ Decimal(3)
print(output)
# 0.3333

getcontext().prec = 2
output = Decimal(1)/ Decimal(3)
print(output)
# 0.33

print(Decimal(3.14))
# 3.140000000000000124344978758017532527446746826171875 👈 this is floating point error
# So to avaoid this we have to use Decimal class with correct input
# 👇 so the correct way is

print(Decimal('3.14'))
# 3.14
# Dealing with the money try to use Decimal class

## Booelan
print(bool(1))
# True
print(bool(-1))
# True
print(bool(1j))
# True
print(bool(0))
# False
print(bool(0.0))
# False
print(bool(0j))
# False

print(bool('True'))
# True
print(bool('False'))
# True
print(bool(''))
# False
print(bool(' '))
# True
print(bool([1,2]))
# True
print(bool({}))
# False
print(bool(None))
# False

myList = [1,2]
if myList:
    print('MyList has some value')

# Boolean Logic
weatherIsNice = False
haveUmbrella = True

if not haveUmbrella or weatherIsNice:
    print('Stay inside')
else: 
    print('Go for walk')