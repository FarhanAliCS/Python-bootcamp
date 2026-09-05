import unittest
class TestEvenAndOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_numbers(n),[12,14,16,18])

    def test_odd(self):
        self.assertEqual(odd_numbers(n),[23,15,17])

def even_numbers(n):
    even_result=[]
    for i in n:
        if i % 2 == 0:
          even_result.append(i)
    return even_result

def odd_numbers(n):
    result=[]
    for i in n:
        if i % 2 != 0:
            result.append(i)
    return result


    

n=[12,23,14,15,16,17,18]
result=even_numbers(n)
result1=odd_numbers(n)
print(result)
print(result1)

if __name__=="__main__":
      unittest.main()