# print number from 1 till 100 
# if number is div by 3 print Fizz, 
# if number is div by 5 Buzz 
# if both then FizzBuzz 
# else number it self.

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

fizzBuzz = FizzBuzz()
fizzBuzz.second_function()
