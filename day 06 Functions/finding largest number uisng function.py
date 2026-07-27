#function return a,b,c
def largest():
    a=int(input("\nEnter  value of a :"))
    b=int(input("Enter  value of b :"))
    c=int(input("Enter  value of c :"))
    if a > b and a > c:
        return a
    elif b > a  and b > c:
        return b
    else:
        return c
   #display 
largest_number=largest()
print("\n Largest is ",largest_number)
    