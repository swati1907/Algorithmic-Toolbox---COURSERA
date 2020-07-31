# Uses python3
import sys

def get_majority_element(a):
    c=0
    count =1 
    m=0
    for i in range(1,len(a)):
        
        if a[i]==a[m]:
            count+=1
        else:
            count+=-1
        if count==0:
            m=i
            count=1
    
    
    for i in a:
        if i==a[m]:
            c+=1 
           
    if c>(n//2):        
        return 1 
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    
    print(get_majority_element(a)) 
    

           
    
