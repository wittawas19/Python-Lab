
print(" *** Summation of each digit ***")
x = int(input("Enter a positive number : "))
y = 0
ten = 10
sum = 0
while x > 0: 
        y = x % 10 
        sum += y
        x =x //10
print("Summation of each digit = " ,sum)
