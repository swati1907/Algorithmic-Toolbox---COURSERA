 #Uses python3

import sys

def greaterthanorequal(i,m):
    return(int(str(i)+str(m))>=int(str(m)+str(i)))
    

    
def largest_number(a):
    b=True
    concat=""
    while(a!=[]):
       m=0
       for i in a:
           if greaterthanorequal(i,m):
               m=i 
       concat+=str(m)
       a.remove(m)
    return(concat)
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int,input.split()))
    a = data[1:]
    #print(a)
    print(largest_number(a))
     
