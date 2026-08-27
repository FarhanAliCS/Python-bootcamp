def generator():
    n=5
    for num in range(1,n):
        yield num

next_number=generator()
print(next(next_number))
print(next(next_number))
print(next(next_number))