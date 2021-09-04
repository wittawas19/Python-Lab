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


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)
        
     
         