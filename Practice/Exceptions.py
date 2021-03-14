#Raise Exception !
# x = -5
# if x < 0:
#     raise Exception('Raise Exceptions: X value should be Positive')

#Assert Exception !
#raise-if-not x>=0
#It runs if not true
# x = -5
# assert (x >=0),'Assert Exception: X should be positive'

#try: except !
try:
    a = 5/0
except:
    print('An error happend')

#try: except catch type of error !
try:
    a = 5/0
except Exception as error:
    print(error)

#It is good practice to specify the type of exception we want to catch
try:
    a = 5
    b = a / '0'
except ZeroDivisionError as error:
    print(error)
except TypeError as error:
    print(error)
else:
    print('Everything is fine')
finally:
    print('cleaning up')

# Defining our own Exception
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too High')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)

try:
    test_value(1)
except ValueTooHighError as error:
    print(error)
except ValueTooSmallError as error:
    print(error.message, error.value)