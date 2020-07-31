# python3
import sys


def compute_min_refills(distance, tank, stop, n):
    # write your code here
    numrefill=0
    currentrefill=0
    lastrefill=0 
    i=0
    ##if ((n==0 and distance>tank) or stop[0]>tank):
        #return -1
    #if (n==0 and distance<tank):
        #return 0
        
    stop.insert(0,0)
    stop.append(distance)
    while(i<=(n)):
        if ( (stop[i+1] - stop[i]) > tank ):
            return(-1)
        i=i+1    
    #print(stop)
    while(currentrefill<=(n)):
        #print(currentrefill, stop[currentrefill])
        lastrefill=currentrefill
        while(currentrefill<=n and (stop[currentrefill+1] - stop[lastrefill]) <=tank):
            currentrefill= currentrefill + 1
        
        numrefill=numrefill+1 
    return numrefill-1
        
    

if __name__ == '__main__':
    d, m, n, *stop = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stop, n))
