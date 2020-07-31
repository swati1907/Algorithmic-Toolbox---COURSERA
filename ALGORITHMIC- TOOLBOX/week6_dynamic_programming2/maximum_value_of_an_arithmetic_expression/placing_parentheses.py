# Uses python3
import math
def evalt(i,j,MIN,MAX,op):
    
    min_=math.inf#assigning infinity
    max_=-math.inf#assigning minus infinity
    for k in range(i,j):
        
        if op[k] == '+':
            a=MAX[i][k]+MAX[k+1][j]
            b=MAX[i][k]+MIN[k+1][j]
            c=MIN[i][k]+MIN[k+1][j]
            d=MIN[i][k]+MAX[k+1][j]
             
        elif op[k] == '-':
            a=MAX[i][k]-MAX[k+1][j]
            b=MAX[i][k]-MIN[k+1][j]
            c=MIN[i][k]-MIN[k+1][j]
            d=MIN[i][k]-MAX[k+1][j]
            
        else :
            a=MAX[i][k]*MAX[k+1][j]
            b=MAX[i][k]*MIN[k+1][j]
            c=MIN[i][k]*MIN[k+1][j]
            d=MIN[i][k]*MAX[k+1][j]
             
        
        max_=max(max_,a,b,c,d)
        min_=min(min_,a,b,c,d)
    return (min_,max_)

def get_maximum_value(dataset):
    m=len(dataset)
    num=dataset[:m:2]
    op=dataset[1:m:2]
    n=len(num)
    MIN=[[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        MIN[i][i]=int(num[i])
    MAX=[[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        MAX[i][i]=int(num[i])
       
   
    for s in range(1,n):
        for i in range(0,n-s):
            #j-i=s
            j=i+s
            MIN[i][j],MAX[i][j]=evalt(i,j,MIN,MAX,op)
           
            
     
    return MAX[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
