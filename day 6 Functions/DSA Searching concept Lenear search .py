#Linear Search 
def lenear_search (numbers,target):
    found=False
    for i in range(len(numbers)):
        if numbers[i]==target:
               return i
                  
    return -1
 #display       
numbers=[11,12,14,14,15,17,36,45]
target=int(input("Enter the target :"))
print(lenear_search(numbers,target))

