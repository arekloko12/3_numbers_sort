a = int(input("Enter the 1-st number "))
b = int(input("Enter the 2-nd number "))
c = int(input("Enter the 3-td number "))

table_of_numbers = []

if a >= b:
    if a >= c:
        table_of_numbers.append(str(a)+"(a)")
        if b >= c:
            table_of_numbers.append(str(b)+"(b)")
            table_of_numbers.append(str(c)+"(c)")
        else:
            table_of_numbers.append(str(c)+"(c)")
            table_of_numbers.append(str(b)+"(b)")
    else:
        table_of_numbers.append(str(c)+"(c)")
        table_of_numbers.append(str(a)+"(a)")
        table_of_numbers.append(str(b)+"(b)")
else:
    if b >= c:
        table_of_numbers.append(str(b)+"(b)")
        if a >= c:
            table_of_numbers.append(str(a)+"(a)")
            table_of_numbers.append(str(c)+"(c)")
        else:
            table_of_numbers.append(str(c)+"(c)")
            table_of_numbers.append(str(a)+"(a)")
    else:
        table_of_numbers.append(str(c)+"(c)")
        table_of_numbers.append(str(b)+"(b)")
        table_of_numbers.append(str(a)+"(a)")

for i in range(3):
    print(table_of_numbers[i], end=", ")

# Author - arekloko
