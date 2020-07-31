# Uses python3
import sys

def optimal_weight(W, g_bars):
    m=len(g_bars)
    gold=[[0 for x in range(W+1)]for y in range(m+1)]
    #filling result row by row
    for i in range(1,m+1):
        for w in range(1,W+1):
            gold[i][w]=gold[i-1][w]
            if g_bars[i-1]<=w:
                val=gold[i-1][w-g_bars[i-1]] + g_bars[i-1]
                if val>gold[i][w]:
                    gold[i][w]=val
                    
    return gold[m][W]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
