def generaor(numbers):
    for n in numbers:
        if n > 10 :
            yield n
    raise StopIteration
numbers=[1,5,7,9,10,49,34,54,23,78]
numbers=generaor(numbers)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
