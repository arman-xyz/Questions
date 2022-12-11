import re
 
def isValid(num):
     
    Pattern = re.compile(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}")
    return Pattern.match(num)
 
# Driver Code
num = input('enter a number : ')
if (isValid(num)):
    print ("Valid Number")    
else :
    print ("Invalid Number")


