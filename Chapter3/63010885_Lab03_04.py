from typing import Sized


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

s = Stack()

n = input('Enter Input : ').split(',')
ans = 0 
treeHighest = 0 
seqTree = 0
for i in range(len(n)) :
    if "A " in n[i] : 
        strSub = int(n[i].replace("A ",""))
        s.push(strSub)
    elif "B" in n[i] :
        strSub = str(n[i])
        s.push(strSub) 
for j in range(0 , s.size()) : 
    if s.items[j] == "B" :
            
            for treeBack in range(j,-1,-1) : 
                if s.items[treeBack] != "B"  :  
                    treeHighest = s.items[treeBack]
                    ans += 1
                    seqTree = treeBack
                    break
            for k in range(seqTree , -1 , -1 ):
                   if s.items[k] != "B" : 
                        if  treeHighest  < s.items[k] :
                            treeHighest = s.items[k]
                            ans += 1
            print(ans)
            ans = 0 