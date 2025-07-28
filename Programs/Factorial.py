# Calculate the factorial of a number

num = int(input("Enter the number you want to check the factorial of : "))

if num < 1:
    print("It is undefined. ")
else:
    result =  1
    for i in range(2, num + 1):
        result *= i

    print(f"{num} factorial is {result}")

