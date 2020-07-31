#Uses python3

import sys

def lcs3(s,t,r):
    n=len(s)
    m=len(t)
    p=len(r)
    result=[[[0 for x in range(m+1)] for y in range(n+1)]for z in range(p+1)]
    #for insertion,deletion,unmatch we add one while for match we add nothing
    for k in range(1,p+1):
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if  s[i-1]==t[j-1] and t[j-1]==r[k-1] :
                    result[k][i][j]=result[k-1][i-1][j-1]+1
                else:
                    result[k][i][j]=max(result[k-1][i][j],result[k][i-1][j],result[k][i][j-1])
    return(result[p][n][m])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    
    print(lcs3(a, b, c))
