import time

def decorator(function):
    def wrapper(*args, **kwargs):
        print("===== Timer start ====")
        start=time.time()
        result=function(*args , **kwargs)
        end=time.time()
        exccution_time=end - start
        print("Total time :",exccution_time)
        return result
    return wrapper

@decorator
def add(a,b):
    return a+b

result=add(12,14)
print("result :",result)