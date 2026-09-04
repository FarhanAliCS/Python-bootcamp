def calculate_average(marks:list[int])->bool:
    averge=sum(marks)/len(marks)
    return averge

marks=[89,34,45,56,67]
average=calculate_average(marks)
print("Average is :",average)