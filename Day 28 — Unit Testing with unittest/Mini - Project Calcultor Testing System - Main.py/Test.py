from Calculator import *
import unittest
class TestCalculator(unittest.TestCase):
      def test_additon(self):
            self.assertEqual(addition(12,4),16)
            self.assertEqual(addition(-1,-1),-2)
            self.assertEqual(addition(1,-1),0)

      def test_subtraction(self):
            self.assertEqual(subtraction(12,4),8)
            self.assertEqual(subtraction(-1,-1),0)
            self.assertEqual(subtraction(-1,1),-2)

      def test_multiplicaion(self):
            self.assertEqual(multiplication(12,2),24)
            self.assertEqual(multiplication(0,0),0)
            self.assertEqual(multiplication(-1,-1),1)

      def test_division(self):
            self.assertEqual(division(12,2),6)
            with self.assertRaises(ZeroDivisionError):
                  division(12,0)




if __name__ == "__main__":
      unittest.main()
            


