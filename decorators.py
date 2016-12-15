"""
    Python decorator example
"""


def my_decorator(msg='Default Welcome Message'):
    def decorated(fnc):
        def wrapper(*args, **kwargs):
            print('The message is: ' + msg)
            print('Before calling the function')
            fnc(*args, **kwargs)
            print('After calling the function')

        return wrapper

    return decorated


@my_decorator('Hi!')
def print_name(name):
    return print(name)


print_name('Ertugrul')
