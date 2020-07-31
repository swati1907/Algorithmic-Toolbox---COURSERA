# Uses python3
import sys

def optimal_summands(n):
    sums=0
    summands = []
    if( n==1):
        summands.append(1)
        return summands
    #write your code 
    for i in range(1,n):
        sums=sums+i
        if((n-sums)>(i)):
            summands.append(i)
        else:
            summands.append(i+n-sums)
            return summands
            break
    ##return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
