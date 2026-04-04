import time

def timer(func):
    def wrapper(*args,**kwargs):
        strat_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()

        print(f"function {func.__name__} ran in {end_time - strat_time}")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)