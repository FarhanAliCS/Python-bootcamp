
        # ==========================
# LIST UTILITY PROGRAM
# ==========================

# Print List
def print_list(numbers):
    if len(numbers) == 0:
        print("List is empty.")
    else:
        print("List:", numbers)


# Largest Number
def largest_number(numbers):
    if len(numbers) == 0:
        print("List is empty.")
    else:
        print("Largest Number:", max(numbers))


# Smallest Number
def smallest_number(numbers):
    if len(numbers) == 0:
        print("List is empty.")
    else:
        print("Smallest Number:", min(numbers))


# Sum of Numbers
def sum_numbers(numbers):
    if len(numbers) == 0:
        print("List is empty.")
    else:
        print("Sum:", sum(numbers))


# Average
def average(numbers):
    if len(numbers) == 0:
        print("List is empty.")
    else:
        total = sum(numbers)
        avg = total / len(numbers)
        print("Average:", avg)


# Count Even Numbers
def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    print("Even Numbers:", count)


# Count Odd Numbers
def count_odd(numbers):
    count = 0

    for num in numbers:
        if num % 2 != 0:
            count += 1

    print("Odd Numbers:", count)


# Linear Search
def search_number(numbers):
    if len(numbers) == 0:
        print("List is empty.")
        return

    target = int(input("Enter number to search: "))

    for i in range(len(numbers)):
        if numbers[i] == target:
            print(target, "found at index", i)
            return

    print(target, "not found.")


# Reverse List
def reverse_list(numbers):
    if len(numbers) == 0:
        print("List is empty.")
    else:
        numbers.reverse()
        print("Reversed List:", numbers)


# Sort List
def sort_list(numbers):
    if len(numbers) == 0:
        print("List is empty.")
    else:
        numbers.sort()
        print("Sorted List:", numbers)


# Remove Duplicate Values
def remove_duplicates(numbers):

    if len(numbers) == 0:
        print("List is empty.")
        return

    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    numbers.clear()

    for num in new_list:
        numbers.append(num)

    print("Duplicates Removed.")
    print(numbers)


# ==========================
# Main Menu
# ==========================
numbers=[12,11,10,14,15,16,17,19,44,32]

while True:

    print("\n========== LIST MENU ==========")
    print("1. Print List")
    print("2. Largest Number")
    print("3. Smallest Number")
    print("4. Sum")
    print("5. Average")
    print("6. Count Even")
    print("7. Count Odd")
    print("8. Search")
    print("9. Reverse")
    print("10. Sort")
    print("11. Remove Duplicates")
    print("12. Exit")
    print("===============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        print_list(numbers)

    elif choice == "2":
        largest_number(numbers)

    elif choice == "3":
        smallest_number(numbers)

    elif choice == "4":
        sum_numbers(numbers)

    elif choice == "5":
        average(numbers)

    elif choice == "6":
        count_even(numbers)

    elif choice == "7":
        count_odd(numbers)

    elif choice == "8":
        search_number(numbers)

    elif choice == "9":
        reverse_list(numbers)

    elif choice == "10":
        sort_list(numbers)

    elif choice == "11":
        remove_duplicates(numbers)

    elif choice == "12":
        print("Thank you for using List Utility Program.")
        break

    else:
        print("Invalid Choice.")


    









