def greet():
    print("HIllo Friends")

def decorator(function):
    def wrapper():
        print("Before function ")
        function()
        print("After function ")
    return wrapper

greet=decorator(greet)
greet()




