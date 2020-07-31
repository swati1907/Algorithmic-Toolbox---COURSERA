#Uses python3
import sys
import math
from itertools import permutations


def minimum_distance(p1,p2):
    #write your code here
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def closest_split_pair(px,py,delta):
    mid=len(px)//2 
    #print(delta,px,"delta,py inclosest split pair")
    xmid=px[mid-1][0]
    #print(xmid,"xmid")
    sy = [x for x in py if xmid - delta <= x[0] <= xmid + delta]

    #print(sy,"list for sx in closest split pair")
   
    best=delta
    for i in range(0,len(sy)-1):
        for j in range(1+i,min(i+5,(len(sy)))):
            d3=minimum_distance(sy[i],sy[j])
            if(d3<best):
                best=d3
    return best            
def comparing(px):
    #print("in loop",px)
    m=minimum_distance(px[0],px[1])
   
    p1 = px[0]
    p2 = px[1]
    ln_px = len(px)
    if ln_px == 2:
        return m
    for i in range(ln_px-1):
        for j in range(i + 1, ln_px):
            if i != 0 and j != 1:
                d = minimum_distance(px[i], px[j])
                if d < m:  # Update min_dist and points
                    m = d
     
    return m   
    
def closest_pair(px,py):
    if len(px)<=3:
        return comparing(px)
            
            
    
    mid=len(px)//2
    qx=px[:mid]
    rx=px[mid:]
    qy=[]#qx sorted wrt y coordinate
    ry=[]#rx sorted wrt y coordinated
    
    for i in py:
        if i[0]<px[mid][0]:
            qy.append(i)
        else:
            ry.append(i)
    #print(qx,qy,"these are qx qy")##################################################
    d1=closest_pair(qx,qy)
    #print(d1,"d1")
    #print(rx,ry,"these are rx,ry")
    d2=closest_pair(rx,ry)
    #print(d2,"d2")
    #print(d1,d2,"d1 &d2")
    dist=min(d1,d2)
    
    #print("dist",dist)
    d3=closest_split_pair(px,py,dist)#here we send opx, py aswe need both qx,qy,rx,ry
    if d3<=dist:
        dist=d3
        return d3
    else:
        return dist
if __name__=="__main__":        
    N=int(input())
    points= [list(int(x) for x in input().split()) for i in range(N)]#outer loop is needd for iteration
    #print(points)######################################################################################
    py= sorted(points,key=lambda x:(x[1],x[0]))#sorting without replacing the original file
    px=sorted(points,key=lambda x:x[0])
    #print(px)##################################################################################################
    #print(py)
    print("{0:.3f}".format(closest_pair(px,py)))

