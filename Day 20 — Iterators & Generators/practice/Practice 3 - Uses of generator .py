#Generator with a numbers 
def numbers(numbers):
    for n in numbers:
        yield n
num=[20,30,40,50]
number=numbers(num)
print(next(number))
print(next(number))
print(next(number))

    