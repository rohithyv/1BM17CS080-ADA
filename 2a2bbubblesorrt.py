#selection sort
print("\n\n selection sort\n\n")

def sel_sort_kth_smallest(a,k):
    for i in range(0,k):
        mini = i
        for j in range(i+1,len(a)):
            if a[j]<a[mini]:
                mini = j
        a[mini],a[i] = a[i],a[mini]
        
    return a[k-1]

        
a = []
n = int(input("Enter the number of elements into an array:"))
for i in range(0,n):
    m = int(input())
    a.append(m)

k = int(input("Enter the value of k:"))
    

print(sel_sort_kth_smallest(a,k))


#bubble sort

print("\n\nbubble sort\n")
def bub_sort_kth_smallest(a,k):
    for i in range(0,k):
        for j in range(0,len(a)-1-i):
            if a[j+1]<a[j]:
                a[j],a[j+1] = a[j+1],a[j]
    return a[k-1]


a = []
print("Enter 5 elements into an array:")
for i in range(0,5):
    t = int(input())
    a.append(t)
    
k = int(input("Enter the value of k:"))

print(bub_sort_kth_smallest(a,k))
