# Uses python3
import sys

def get_change(money):
    
    #basic idea is to use dynamic programming to calculate all the possible results of sub-problems to re-use them for finding the final solution
    if money ==1:
        return 1
    coins=[1,3,4]
    mn=[0]*(money+1)#A dynamic programming array
    mn[0]=0
    for m in range(1,money+1):
        
        mn[m]=m
        for i in coins:
            if m>=i:
                num=mn[m-i]+1 
                
                if num<mn[m]:
                    
                    mn[m]=num
    
    return mn[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
