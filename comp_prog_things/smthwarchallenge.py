import math

def narcissistic( value ):
    narlen = len(str(value))
    narvar = 0
    for i in range(narlen):
        narvar = narvar+int(str(value)[i:i+1])**narlen
    if(narvar == value):
        return True
    else:
        return False
print(narcissistic(128851796696487777842012787))