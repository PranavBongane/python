import time 
def cache(func):
    cash_value = {}
    print(cash_value)
    def wrapper(*args):
        if args in cash_value:
            return cash_value[args]
        result = func(*args)
        cash_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))