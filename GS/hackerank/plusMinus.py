def plusMinus(arr):
    # Write your code here
    #initialize counters for positive, negative and zero
    pc = 0 #positive count
    nc =0  #negative count
    zc =0  #zero count
    
    #iterate through the array and count the elements
    for num in arr:
        if num > 0:
            pc += 1
        elif num < 0:
            nc += 0
        else:
            zc += 1
            
#calculate the ratios
 #pr = positive ratio
 #nr = negative ratio
 #zr = zero ratio
    tc = len(arr)
    pr = pc/ tc
    nr = nc/tc
    zr = zc/tc
    
    return pr, nr, zr
                 