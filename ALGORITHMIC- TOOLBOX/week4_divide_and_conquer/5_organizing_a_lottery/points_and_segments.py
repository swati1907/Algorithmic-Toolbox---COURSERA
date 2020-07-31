 
# Uses python3
import sys
import random



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    numbers=starts+ends+points
    left=1 
    right=3 
    point=2 
    start_l=[left]*len(starts)
    points_p=[point]*len(points)
    ends_r=[right]*len(ends)
    numbers_l_p_r=start_l+ends_r+points_p
    #print(numbers,numbers_l_p_r)
    num=list(zip(numbers,numbers_l_p_r))
    
    #randomized_quick_sort(num,0,len(num)-1)
    num.sort(key=lambda x:(x[0],x[1]))
    #print(num)
    count={}
    cnt=0
    for i in num:
        if i[1]==1:
            cnt+=1 
        elif i[1]==3:
            cnt+=-1
        elif i[1]==2:
            count[i[0]]=cnt
    for i in points:
        print(count[i],end=" ")
            

