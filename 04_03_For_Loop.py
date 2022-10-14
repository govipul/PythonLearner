
animalLookup = {
            'a':['antelope','aardvark'],
            'b':['bear'],
            'c':['cat'],
            'd':['dog'],
        }

class ForLoop:
     
    def start(self):
        myList = [1,2,3,4,5]
        for item in myList:
            print(item)
    def version1(self):
        for letter, animal in animalLookup.items():
            pass
    def version2(self):
        for letter, animals in animalLookup.items():
            if len(animals) > 1 :
                continue
            print(f'Only one animal {animals[0]}')


forLoop = ForLoop()
forLoop.start()
forLoop.version1()
forLoop.version2()