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
     
    
     
def match(open,close):
     if open != '' and close != '' : 
          return (open == '(' and close == ")") or (open == '{' and close == "}") or (open == '[' and close == "]")    


def parenMatching(string): 
     s = Stack() 
     check = 0
     for i in range(len(string)) :
          char = string[i]
          if char in ["(","{","["] : 
               s.push(char)

          elif char in [")","}","]"]  :
               if s.size() > 0 : 
                    if not match(s.pop(),char) :
                        print(string ,"Unmatch open-close")
                        s.items = []
                        check = 1 
                        break

               elif s.size() == 0 and  i != len(string) :
                     print(string, "close paren excess")  
                     check = 1 
                     break

              
     if s.size() > 0  and check == 0:
          print(string,"open paren excess  ",s.size(),":",end=" ")
          print(*s.items,sep="")               
     
     elif s.size() == 0 and check == 0 : 
          print(string , "MATCH")
          
             

string = input("Enter expresion : ")
parenMatching(string)