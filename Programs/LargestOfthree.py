# Find the largest of three numbers

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if c < a >b :
    print(f"{a} is the biggest number ")
elif a < b > c:
    print(f"{b} is the biggest number  ")
else:
    print(f"{c} is the biggest number ")
