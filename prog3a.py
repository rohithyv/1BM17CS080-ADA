#Python program for implementation of mergesort

def mergesort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]#dividing the array
        R = arr[mid:]#elements into 2 halves

        mergesort(L) #sorting the first half
        mergesort(R) #sorting the right half

        i = j = k = 0

        #copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[i]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1


            #checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

       
        def printList(arr):
            for i in range(len(arr)):
                print(arr[i],end=" ")
                print()

                if __name__ == '__main__':
                    arr = [12, 11, 13, 5, 6, 7]
                    print ("Given array is", end="\n")
                    printList(arr)
                    mergeSort(arr)
                    print("Sorted array is: ", end="\n")
                    printList(arr) 
  

        
