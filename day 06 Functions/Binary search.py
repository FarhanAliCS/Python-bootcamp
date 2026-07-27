#Binary search
def binary_search(numbers,target):
    low=0
    high=len(numbers)-1
    while low <=high:
        mid=(low + high)//2
        if numbers[mid]==target:
            return mid
        elif target > numbers[mid]:
            low=mid+1
        else:
            high=mid-1

#main menue
numbers=[12,13,14,15,16,17]
target=int(input("Enter the target :"))
result=binary_search(numbers,target)
print(result)
           
