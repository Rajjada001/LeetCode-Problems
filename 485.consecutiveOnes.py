def consecutiveOnes(a):
# [1,1,1,0,1,1,0] => 3
    curr_ones = max_val = 0
    for i in range(len(a)):
        if a[i]==1:
            curr_ones += 1
            max_val = max(curr_ones,max_val)
        else:
            curr_ones = 0
    
    return max_val


print(consecutiveOnes([1,1,1,0,1,0,1,1]))
print(consecutiveOnes([1,1,0,0,1,0,1,1]))
print(consecutiveOnes([1,0,1,0,1,0,1,1]))
print(consecutiveOnes([1,1,1]))