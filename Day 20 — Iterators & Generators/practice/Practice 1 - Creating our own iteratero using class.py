class Mynumbers:
    def __iter__(self):
        self.number =1
        return self


    def __next__(self):
        if self.number <= 5 :
            result=self.number
            self.number += 1
            return result
        else:
            raise StopIteration

numbers=Mynumbers()
iterator=iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


         