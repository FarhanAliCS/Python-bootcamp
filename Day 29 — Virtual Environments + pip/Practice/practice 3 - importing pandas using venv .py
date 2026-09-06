import pandas as pd

# Practic of pandas using vertual environment 

data={
    "Name":["Ali","Farhan","Ayan","Ahmed","Usman","Ayesha"],
    "Age": [20,21,22,23,24,21,],
    "Marks":[85,72,75,66,90,95]
}

dataframe=pd.DataFrame(data)

total_students=dataframe.shape[0]


average=dataframe["Marks"].mean()


highestmarks=dataframe["Marks"].max()

lowestmarks=dataframe["Marks"].min()


print("--------: Student info :--------------")
print(dataframe,"\n")
print(":-----------------------------------:")
print("Number of Students :",total_students)
print("Average Marks      :",average)
print("highest_marks      :",highestmarks)
print("Lowest marks       :",lowestmarks)
print(":--------------------------------------:")
