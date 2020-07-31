# Uses python3
def edit_distance(s, t):
    n=len(s)
    m=len(t)
    result=[[0 for x in range(m+1)] for y in range(n+1)]
    
    for i in range(n+1):
        result[i][0]=i
    #for insertion,deletion,unmatch we add one while for match we add nothing
    for j in range(1,m+1):
        result[0][j]=j
        for i in range(1,n+1):
            insert=result[i][j-1]+1
            delete=result[i-1][j]+1 
            match=result[i-1][j-1]
            unmatch=result[i-1][j-1]+1 
            
            if  s[i-1]==t[j-1]:
                result[i][j]=min(insert,delete,match)
            else:
                result[i][j]=min(insert,delete,unmatch)
        
       
       
    #write your code here
    return result[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
