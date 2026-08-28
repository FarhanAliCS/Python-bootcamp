def decorator(function):
    def wrapper(*args ,**kwargs):
        print("Beofore .")
        function(*args , ** kwargs)
        print("After .")
    return wrapper

@decorator
def add(a,b):
    print(a+b)

add(12,12)
