print("*** Fun with countdown ***")
text = input("Enter List : ")
number = []
seq = []
temp = []
extend = []
Answer = []
x = (text.split(" "))
for i in x:
  number.append(int(i))
number.append(0)
for i in range(0,len(number)-1) :
    if (number[i] == (number[i+1]+1)) and (i < len(number)) and number[i] != 1 :
        temp.append(number[i])
    if number[i] == 1 and number [i-1]==number [i]+1 :
        temp.append(number[i])
    if number[i] == 1 and number [i-1]!=number [i]+1 :
        temp.append(number[i])
temp.append(0)

for i in range(0,len(temp)-1) :
    if temp[i] !=1 :
       extend.append(temp[i]) 
    else :
        extend.append(temp[i])
        seq.append(extend)
        extend = []

Answer.append(len(seq))
Answer.append(seq)
print(Answer)