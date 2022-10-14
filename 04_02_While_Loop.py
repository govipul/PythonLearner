from datetime import datetime

class WhileStatement:
        def start(self):
            print(datetime.now())   
            print(datetime.now().second)

        def waitUntil(self):
            print('This is a version 1')
            wait_until = datetime.now().second + 2
            while datetime.now().second != wait_until : 
                print('Still waiting....')
            print(f'we are {wait_until} seconds!')
        
        def waitUntil2(self):
            print('This is a version 2')
            wait_until = datetime.now().second + 2
            while datetime.now().second != wait_until : 
                pass # its a continue statement like in Java
            print(f'we are {wait_until} seconds!')

        def waitUntil3(self):
            print('This is a version 3')
            wait_until = datetime.now().second + 2
            while True: 
                if datetime.now().second == wait_until :
                    break # its break statement like in Java and break only 1 loop statement
            print(f'we are {wait_until} seconds!')

        def waitUntil4(self):
            print('This is a version 4')
            wait_until = datetime.now().second + 2
            while True: 
                if datetime.now().second < wait_until :
                    continue 
                break 
            print(f'we are {wait_until} seconds!')

whileObj = WhileStatement()
whileObj.start()
whileObj.waitUntil()
whileObj.waitUntil2()
whileObj.waitUntil3()
whileObj.waitUntil4()