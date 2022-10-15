## class CustomException(Exception):
#    pass
#def causeError():
#    raise CustomException('You called cause Error method')

#causeError()

class HttpExcpetion(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'status code: {self.statusCode} and message is: {self.message}')

class NotFoundException(HttpExcpetion):
    statusCode = 404
    message = 'Resource Not found'

class ServerError(HttpExcpetion):
    statusCode = 500
    message = 'The server messed up'

def raiseServerError():
    raise ServerError()

raiseServerError()