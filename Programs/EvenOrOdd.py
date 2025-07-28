# Check if the number is  even or odd

num = int(input("Enter the number you want to check if it is prime or not : "))

if num < 1:
    print("It is not a prime number")
elif num == 2:
    print("It is a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
