def generator():
    for n in range (1,10+1):
        if n %2 == 0:
            yield n

numbers=generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))