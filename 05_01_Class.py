class Dog:
    _legs = 4 # Note here '_' doesnt add any restriction but 
              # just indicate that these are class variables and must not be refer to them directly.
    def __init__(self, name) -> None:
        self.name = name
    
    def getLegs(self) -> int :
        return self._legs

    def speak(self) -> None:
        print(f'{self.name} says: bark')


myDog = Dog('Tommy')
print(myDog.name)
print(myDog.getLegs())
myDog.speak()
