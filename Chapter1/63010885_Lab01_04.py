print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
n += 1
i = 0 
for col  in range(1,n):
    for row in range(2,(2*n)-1):
        if col + row == n+1  or row - col == n-1 :
            print("*",end="") 
        elif row-col >= n  or row + col <= n or col == 1    : 
            print(".",end="") 
        else : 
             print("+",end="")
    for row in range(3,(2*n)-1):
        if col + row == n+1  or row - col == n-1 :
            print("*",end="") 
        elif row-col >= n  or row + col <= n or col == 1    : 
            print(".",end="") 
        else : 
             print("+",end="")
    print()
n = n-1 
for col in range(0,(2*n)-2) :
    for row in range(0,(3*n)+(n-3)) :
        if row - col == 1 or row + col == 3*n+(n-5):
          print("*",end="")
        elif row - col <= 0 or  row + col >= (3*n) + (n-4):
            print(".",end="") 
        else : 
          print("+",end="")
    print()
    