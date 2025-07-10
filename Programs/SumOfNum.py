# Calculate the sum of numbers from 1 to 100

num = int(input("Number you want the sum until : "))

if num<=0:
     print("Enter a positive number : ")
else :
    total = 0

    for x in range(1,num + 1):
        total = total + x
    print(total)