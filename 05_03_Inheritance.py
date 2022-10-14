class Dog:
    _legs = 4 # Note here '_' doesnt add any restriction but 
              # just indicate that these are class variables and must not be refer to them directly.
    def __init__(self, name) -> None:
        self.name = name
    
    def getLegs(self) -> int :
        return self._legs

    def speak(self) -> None:
        print(f'{self.name} says: bark')

class Chihuahua(Dog):
    pass

class Chihuahua2(Dog):
    def speak(self) -> None:   # Override method in inheritance
        print(f'{self.name} name: Yep yep')
    
    def vagTail(self) -> None:
        print('Wagging')

myDog = Chihuahua('Roxy')
myDog.speak()
myDog2 = Chihuahua2('Tummy')
myDog2.speak()
myDog2.vagTail()


class UniqueList(list):
    def __init__(self) -> None:
        super().__init__()
        self.someProperty = 'Unique List Data'


    def append(self, __object: int) -> None:
        if __object in self:
            return 
        super().append(__object)

myList = UniqueList()
myList.append(1)
myList.append(1)
myList.append(2)
print(myList)
print(myList.someProperty)
## Output 
# [1, 2]
# Unique List Data