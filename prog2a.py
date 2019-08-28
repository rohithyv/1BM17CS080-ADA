#selection sort
print("\n\n The smallest kth element\n\n")
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
        for j in range(0,len(a)-i-1):
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



#Largest element
print("\n\n The largestKth element program\n\n")

#selection sort

def sel_sort_kth_largest(a,k):
    for i in range(0,k):
        maxi = i
        for j in range(i+1,len(a)):
            if a[j]>a[maxi]:
                maxi = j
        a[maxi],a[i] = a[i],a[maxi]
        
    return a[i]

        
a = []
print("Enter 5 elements into an array:")
for i in range(0,5):
    t = int(input())
    a.append(t)

k = int(input("VALUE OF K:"))
    

print(sel_sort_kth_largest(a,k))


#bubble sort

def bub_sort_kth_largest(a,k):
    for i in range(0,k):
        for j in range(0,len(a)-i-1):
            if a[j+1]>a[j]:
                a[j],a[j+1] = a[j+1],a[j]
    for i in range(0,i+1):
        print(a[i])

a = []
print("Enter 5 elements into an array:")
for i in range(0,5):
    t = int(input())
    a.append(t)
    
k = int(input("Enter the value of k:"))

print(bub_sort_kth_largest(a,k))

