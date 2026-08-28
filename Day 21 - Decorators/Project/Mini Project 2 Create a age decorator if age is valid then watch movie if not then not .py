def check_age(function):
    def wrapper():
        age=int(input("Enter your age :"))
        if age >= 18 :
            function()
        else:
            print("You are not allowed to watch movie .")
    return wrapper

@check_age
def watch():
    print("Movie started .")

watch()


