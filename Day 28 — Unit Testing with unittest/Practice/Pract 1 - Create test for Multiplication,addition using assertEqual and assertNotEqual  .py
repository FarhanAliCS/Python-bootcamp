import unittest
class CheckMultiplication(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(12,3),36)

    def test_addition(self):
        self.assertNotEqual(addition(12,5),34)
        

def multiply(a,b):
    return a*b

def addition(a,b):
    return a+b

if __name__=="__main__":
    unittest.main()



