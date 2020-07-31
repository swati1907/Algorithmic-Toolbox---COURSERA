# Uses python3
import sys
'''Input:
5 1 5 8 12 13
5 8 1 23 1 11
Output:
2 0 -1 0 -1
In this sample, we are given an increasing sequence 𝑎0 = 1, 𝑎1 = 5, 𝑎2 = 8, 𝑎3 = 12, 𝑎4 = 13 of length
five and five keys to search: 8, 1, 23, 1, 11. We see that 𝑎2 = 8 and 𝑎0 = 1, but the keys 23 and 11 do
not appear in the sequence 𝑎. For this reason, we output a sequence 2, 0, −1, 0, −1'''
def binary_search(a, x):
    l, r = 0, len(a)-1
    
    while(l<=r):
        mid=l +(r-l)//2
    
        if(a[mid]==x):
            
            return mid
           
        elif(a[mid]<x):
           l=mid+1
           continue
        else:
            
            r=mid-1
            continue
           
    return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 2:]
    a = data[1 : n + 1]

    for x in m:
        
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
