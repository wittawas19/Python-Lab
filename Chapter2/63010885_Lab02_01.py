class translator:

    def deciToRoman(self, num):

        number = [ 1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rome = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman_Number = ""
        i = 0 
        while num > 0 :
            if num // number[i] :
                roman_Number += rome[i]
                num -= number[i]  
            else :
                i += 1     

        return roman_Number

    def romanToDeci(self, s):
        deciNumber = 0
        romanDict = {
              "I":     1  , "V" :    5  ,  "X" :    10 ,  "L" :    50 ,  "C" :    100 ,"D" :    500 , "M" :    1000 , 
         }
        for i in range(len(s)) :
            if  i +1  != len(s) and  romanDict[s[i]] < romanDict[s[i+1]] :
                deciNumber -= romanDict[s[i]]
            else :
                deciNumber += romanDict[s[i]]

        
        return deciNumber 


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))

