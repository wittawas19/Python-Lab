


def range(*arg) :
    myList = list(map(float,arg))
    ansList = [] 
    nyFormat = "{0:.3f}"
    if len(arg) == 1  :
        end = myList[0]
        start = 0.0
        while end > 0 :
            ansList.append(start)
            start += 1.0
            end -= 1 
    elif len(arg) == 2 :
        start = myList[0]
        end = myList[1]
        while start < end :
            ansList.append(start)
            start += 1
            
    elif len(arg) == 3 :
        start = myList[0]
        end = myList[1]
        step = myList[2]
        while  start < end: 
            ansList.append(float(nyFormat.format(start)))
            start += step 
            
    return tuple(ansList)

print("*** New Range ***")
n = input("Enter Input : ").split()
print(range(*n))


