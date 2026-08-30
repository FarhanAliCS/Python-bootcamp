# Using map(),filter(),sorted(),reduce()
# 1️⃣ Passed Students
# Keep marks >= 50.
# 2️⃣ Add Bonus
# Add 5 marks to every passed student.
# 3️⃣ Sort Marks
# Sort the bonus marks from highest → lowest.
# 4️⃣ Find Total
# 5️⃣ Find Highest
# 6️⃣ Find Average
from functools import reduce
marks = [45, 67, 32, 89, 76, 41, 90, 55, 38, 82]

passed_marks=filter(lambda x :x>=50,marks)

after_bonus=map(lambda x: x+5 ,passed_marks)

sorted_marks=sorted(after_bonus,reverse= True)

total_marks=reduce(lambda a,b:a+b,sorted_marks)

highest_marks=reduce(max,sorted_marks)

average_marks=total_marks/len(sorted_marks)

print("========== STUDENT MARKS ANALYZER ==========")

print("Passed Marks      : 50",)
print("Bonus Marks       : 5",)   
print("Sorted Marks      :",sorted_marks)  
print("Total Marks       :",total_marks) 
print("Highest Marks     :",highest_marks)
print("Average Marks     :",average_marks)
print("=============================================")
