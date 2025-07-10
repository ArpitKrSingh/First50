#Print all even numbers between 1 and 20.

num = int(input("the number you want even numbers until : "))

for x in range(1,num):
    if x % 2 == 0:
        print(x)