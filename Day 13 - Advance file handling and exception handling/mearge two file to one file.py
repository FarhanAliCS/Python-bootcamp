source1="notes.txt"
source2="backup.txt"
destination="destination.txt"

try:
    with open(source1,'r') as file1:
        data1=file1.read()
    with open(source2,'r') as file:
        data2=file.read()

    with open(destination,'w') as d:
        d.write(data1 + " \n" + data2)
except FileNotFoundError as e:
    print("Error :",e)
else:
    print("data copy succesfully .")
