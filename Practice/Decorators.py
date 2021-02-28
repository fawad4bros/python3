def cough_dec(func):
    def func_wrapper():
        #CODE BEFORE FUNCTION
        print('*Cough')
        func()
        #CODE AFTER FUNCTION
        print('*cough')
    return func_wrapper
@cough_dec    
def question():
    print('Discount')
@cough_dec
def answer():
    print('No!')

question()
answer()