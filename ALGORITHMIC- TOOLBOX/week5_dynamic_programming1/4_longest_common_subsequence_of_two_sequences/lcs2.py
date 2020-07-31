#`Uses python3

import sys

def lcs2(s, t):
    
    n=len(s)
    m=len(t)
    result=[[0 for x in range(m+1)] for y in range(n+1)]
    

    #for insertion,deletion,unmatch we add nothing while for match we add 1
    for j in range(1,m+1):
        
        for i in range(1,n+1):
            insert=result[i][j-1]
            delete=result[i-1][j] 
            match=result[i-1][j-1]+1
            unmatch=result[i-1][j-1] 
            
            if  s[i-1]==t[j-1]:
                result[i][j]=match
            else:
                result[i][j]=max(insert,delete,unmatch)
        
    return result[n][m]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
