def threeSum(num , sum = 0) :
    ansList = []
    if len(num) > 2 :
        for i in range( 0, len(num)):
          for j in range(i + 1, len(num)):
             for k in range(j + 1, len(num)):
                    if num[i] == num[j] == num[k] and len(ansList) != 0: 
                                break 
                    else :
                        if num[i] + num[j] + num[k] == sum:
                             myList = [num[i],num[j],num[k]]
                             ansList.append(myList)     
                        
    else :
        return("Array Input Length Must More Than 2")               
    return ansList

n = list(map(int ,input("Enter Your List : ").split()))
print(threeSum(n))


