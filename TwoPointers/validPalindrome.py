def validPalindrome(s):
    # str.replaceAll('[^a-zA-Z]',"")
    # new_string = ''.join(char for char in s if char.isalnum())
    new_string = ''
    for char in s:
        if char.isalnum():
            new_string += char
    new_string = new_string.lower()
    # print(new_string)
    left,right = 0,len(new_string)-1
    if len(new_string)==0:
        return True
    while(left<right):
        if(new_string[left] != new_string[right]):
               return False
        left+=1
        right-=1
    return True


print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))
print(validPalindrome(" "))
print(validPalindrome("93749213874bdfkashdfj392482309874"))