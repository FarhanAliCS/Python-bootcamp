def decorator(function):
    def wrapper(*args , **kwargs):
        print("Function is running .")
        result=function(*args , **kwargs)
        return result
    return wrapper

@decorator
def subtract(a,b):
    return a-b

result=subtract(12,9)
print(result)
        
    
    