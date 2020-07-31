# Uses python3
import sys

def maximum_loot_value(capacity, weights, values):
    value=0
    ratio=[]
    c=sum(weights)
    if c<capacity :
        value = sum(values)
    
    else :
        for i in range(0,len(weights)):
            b=values[i]/weights[i]
            ratio.append(b)
        while(capacity>0):   
            j=ratio.index(max(ratio))
            a=min(weights[j],capacity)
            value=value+a*ratio[j]
            weights[j]=weights[j]-a
            ratio[j]=0
            capacity=capacity-a 
       
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    ##print(n , capacity)
    ##print(len(weights))
    opt_value = maximum_loot_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
