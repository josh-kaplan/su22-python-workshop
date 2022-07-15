"""

Getting started with lists

"""

students = ["Alice", "Bob", "Eve"]

num = 1
for student in students:
    # String concatenation
    #print(str(num) + ". " + student)

    # Format strings
    string_to_print = f"{num}. {student}"
    print(string_to_print)

    # Increment num
    num = num + 1
