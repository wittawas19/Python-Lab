class Stack: 
     def __init__(self,myList = None,sizeStack = 0) :
      if myList == None :
          self.items = [] 
      else : 
          self.items = myList 
      self.sizeStack = len(self.items)
      
     def push(self, i): 
          self.items.append(i)
          self.sizeStack += 1 

     def pop(self): 
          return self.items.pop()
     
     def isEmpty(self) :
          return self.items == []
     
     def size(self):
          return len(self.items)

def dec2bin(decnum):

    s = Stack()
    remider = 0
    ans = ""
    while  decnum != 0 : 
        remider = decnum % 2 
        s.push(int(remider))
        decnum  = (decnum - remider) /  2
    (s.items).reverse()
    for i in range(0,s.size()):
        ans = ans.ljust((i+1),str(s.items[i]))
    return ans 
print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))