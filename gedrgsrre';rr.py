X=0
try:
    try:
        print("start code")
        print(10 / x)
        print('No errors')
    # except NameError as ex:
    #     print(f'We have an error: {ex}')
    # except ZeroDivisionError as ex:
    #     print(f'We have an error: {ex}')
    except SyntaxError as ex:
        print(ex)
except (NameError, ZeroDivisionError) as ex:
    print(f"We have an error: {ex}")

print('code after')

try:
    print("start code")
    print(10 / 0)
    print('No errors')
except (NameError, ZeroDivisionError) as ex:
    print(f"We have an error: {ex}")
else:
    print('i am ELSE!')
finally:
    print('finally code')

def checker(value):
    if not isinstance(value, str):
        raise TypeError(f'Sorry we cannot work with {type(value)},'
                        f'We need only str')

    else:
        return 'Niiicee' + value

#checker(100)

class BuildingError(Exception):
    def __init__(self, amount, limit):

        self.amount = amount
        self.limit = limit

    def __str__(self):
        return (f'Not enought materials to build'
                f' We need at least {self.limit}, but got {self.amount}!')

def check_materials(amount, limit):
    if amount >= limit:
        print('yes! we can build the house')
    else:
        raise BuildingError(amount, limit)

#check_materials(100, 250)


import warnings

# warnings.simplefilter('always', ImportWarning)
# warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('error', ImportWarning)
try:
    warnings.warn('warning, wrong import', ImportWarning)
except:
    print('Warning processed')
