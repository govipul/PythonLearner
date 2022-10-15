import time

def causerError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception as e:
        print(e)
        print(type(e))
    finally:
        print(f'this took {time.time() - start} seconds to execute')

def causerMultipleError():
    try:
        return 1 + 'a'
    except TypeError as typeError:
        print(f'There was type error {typeError}')
    except ZeroDivisionError as zeroDivisionError:
        print(f'There was zero by divide error {zeroDivisionError}')
    except Exception as e:
        print(e)
        print(type(e))
    finally:
        print('We have reached finally')

#### Code for custom decorator
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError as typeError:
            print(f'There was type error {typeError}')
        except ZeroDivisionError as zeroDivisionError:
            print(f'There was zero by divide error {zeroDivisionError}')
        except Exception as e:
            print('There is some error')
            print(type(e))
        finally:
            print('We have reached finally')
    return wrapper

@handleException
def customDecorater():
    return 1/0

## Raise Exception
@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)

causerError()
print('Multiple Error........')
causerMultipleError()
print('Custom Decorator........')
customDecorater()
print('Raise Exception........')
raiseError(0)
