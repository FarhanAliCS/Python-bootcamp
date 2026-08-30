from functools import reduce
numbers = [12, 5, 8, 21, 30, 17, 40, 3, 16]
# Keep only numbers greater than 10.
# Step 2
# From those, keep only even numbers.
# Step 3
# Multiply every remaining number by 3.
# Step 4
# Use reduce() to calculate their total.

final_numbers=filter(lambda x: x > 10 and x % 2 == 0 ,numbers)
result=map(lambda x:x*3 ,final_numbers)
final_result=reduce(lambda a,b:a+b ,result)
print(final_result)

