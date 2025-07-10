# Print a multiplication table for a given number.

num = int(input("Enter the number you want a multiplication table of  : "))

for x in range(1,11):
    print(f"{num} x {x} = {num*x}")