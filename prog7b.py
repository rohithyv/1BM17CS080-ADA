import time


def knapsack(w,v,W):
    V = [[0 for i in range(W+1)]for i in range(len(v))]
    n= len(v)
    for i in range(n):
        for j in range(W+1):
            if j-w[i]>=0:
                V[i][j] = max(V[i-1][j],v[i]+V[i-1][j-w[i]])
            else:
                V[i][j] = V[i-1][j]
    return V,V[n-1][W]

w = [1,2,2,3]
v = [10,12,15,20]
W = 5

t1 = time.time()
print(knapsack(w,v,W))

t2 = time.time()

print(t2-t1)

