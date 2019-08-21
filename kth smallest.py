def kthSmallest(arr, n, k): 
  
    # Sort the given array  
    arr.sort() 
  
    # Return k'th element in the  sorted array 
    return arr[k-1] 
  
 
if __name__=='__main__': 

    arr = []
    l = int(input("Enter the size of the array\n"))
    for i in range(0,l):
        print("\n ")
        t = int(input())
        arr.append(t)
    n = len(arr) 
    
    k = int(input("Enter the position of the smallest element you want\n"))
   
    print("K'th smallest element is\n", kthSmallest(arr, n, k)) 
  
