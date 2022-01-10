
def isPalindrome(n):
    if(n<0):
        return False
    
    string = str(n)
    left,right = 0,len(string)-1

    while(left < right):
        if(string[left] != string[right]):
            return False
        left+=1
        right-=1
    
    return True

t = int(input("Test cases:"))
for _ in range(t):
    print(isPalindrome(int(input())))