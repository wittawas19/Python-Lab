
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

def postFixeval(st):
   
    s = Stack()
    for i in st : 
        if i in ["+","-","*","/"] : 
            x = s.pop()
            y = s.pop()
            s.push(str(eval(y + i + x)))  
        else :
            s.push(i)
           
    return float(s.pop())

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())
ans = postFixeval(token)
print("Answer : ",'{:.2f}'.format(ans))

