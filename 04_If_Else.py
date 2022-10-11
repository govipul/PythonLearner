# print number from 1 till 100 
# if number is div by 3 print Fizz, 
# if number is div by 5 Buzz 
# if both then FizzBuzz 
# else number it self.

from sre_parse import fix_flags


class FizzBuzz:

    def first_function(self):
        for n in range(1,101) :
            if n%15 == 0:
                print('FizzBuzz')
            else:
                if n % 3 == 0:
                    print('Fizz')
                else:
                    if n%5 == 0 :
                        print('Buzz')
                    else:
                        print(n)

    def second_function(self):
        for n in range(1, 101):
            if n % 15 == 0:
                print('FizzBuzz')
            elif n % 3 == 0:
                print('Fizz')
            elif n % 5 == 0:
                print('Buzz')
            else:
                print(n)
    
    def third_function(self):
        n = 3
        print('Fizz' if n % 3 == 0 else n)

        n = 5
        print('Buzz' if n % 5 == 0 else n)

        # This is ternary operator in Python, but its recommended to use the 'elif' instead of this as this is hard for readabilty purpose.
        print(['FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 ==0 else n for n in range(1,101)])

fizzBuzz = FizzBuzz()
print('First Function')
fizzBuzz.first_function()
print('Second Function')
fizzBuzz.second_function()
print('Third Function')
fizzBuzz.third_function()