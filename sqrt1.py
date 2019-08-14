def sqrt(x) : 
  
    
    if (x == 0 or x == 1) : 
        return x 
   
    
    begin = 1
    end = x    
    while (begin <= end) : 
        mid = (begin + end) // 2
          
        
        if (mid*mid == x) : 
            return mid 
              
       
        if (mid * mid < x) : 
            begin = mid + 1
            ans = mid 
              
        else : 
              
           
            end = mid-1
              
    return ans 
  
x=12
 

print(sqrt(x)) 
