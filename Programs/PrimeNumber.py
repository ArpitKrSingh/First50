# Check if a number is prime

num = int(input("Enter the number you want to check if it is prime or not : "))

if num < 2:
    print("It is a prime number. ")
elif num == 2:
    print("It is a prime number. ")
else:
    is_Prime = True
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            is_Prime =  False
            break
    if is_Prime:
        print("It is a prime number. ")
    else:
        print("It is not a prime number. ")

