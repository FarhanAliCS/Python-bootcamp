#1st way of import
import Calculator

#2nd way of import
from Calculator import subtraction

#3rd way of import
import Calculator as c



#1st way use
add=Calculator.addition(12,43)

# 2nd way use
sub=subtraction(12,3)

#3rd way use
multiply=c.multiplication(12,3)


print("--------- Result -----------")
print("Addition :",add)
print("subtraction :",sub)
print("Multiplication :",multiply)




