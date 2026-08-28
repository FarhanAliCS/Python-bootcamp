def decorator(function):
    def wrapper():
        print("Before function execution .")
        function()
        print("After function execution .")
    return wrapper
@decorator
def hillo():
    print("Hillo every one .")

hillo()