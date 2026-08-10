source_file = "source.txt"
destination_file = "backup.txt"

try:
    with open(source_file, "a+") as source:
        source.write("informations .")
        source.seek(0)
        data = source.read()
        print(data)
    with open(destination_file, "a") as destination:
        destination.write(data)

except FileNotFoundError:
    print("Source file not found.")

else:
    print("Content copied successfully.")
