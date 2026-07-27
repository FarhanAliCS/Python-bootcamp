#area of circle
def circle_area():
    radius=int(input("Enter radius :"))
    area=3.14 * radius**2
    return area

#celcius to fahrehete
def fahrenheite_calculation():
                  celcius=int(input("Enter celcius :"))
                  fahrenheite=(celcius*9/5) +32
                  return fahrenheite

area=circle_area()
print('area of circle is :', area)
fahrenheite=fahrenheite_calculation()
print("fahrenheite is :",fahrenheite)