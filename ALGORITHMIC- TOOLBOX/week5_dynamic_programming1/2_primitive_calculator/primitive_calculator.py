# Uses python3
import sys

def optimal_sequence(n):
    result=[0]*(n+1)
    sequence = [n]
    if  n==1:
        return([1])
    for i in range(2,n+1):
        temp_2,temp_3=n,n
        temp_1=result[i-1]+1
        if i%3==0:
            temp_2=result[i//3] + 1
        elif i%2==0:
            temp_3=result[i//2]+1
        m=min(temp_2,temp_1,temp_3)
        result[i]=m
      
    while(n>1):
       
        if n%3==0 and result[n//3]==result[n]-1:
            n=n//3
            sequence.append(n)
        elif n%2==0 and result[n//2]==result[n]-1:
            n=n//2
            sequence.append(n)
        else:
            n=n-1
            sequence.append(n)
            
    return(sequence)     
    
 


input = sys.stdin.read()
n = int(input)
sequence=optimal_sequence(n)
n=len(sequence)
print(n-1)
for i in range(0,n):
    print(sequence[n-1-i],end=" ")
    

