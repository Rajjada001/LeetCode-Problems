def firstDuplicate(a):
    s = set()
    for num in a:
        if num in s:
            return num
        s.add(num)
    
    return -1


t = int(input("Enter test cases:"))
for _ in range(t):
    a = list(map(int, input().rstrip().split()))
    print(firstDuplicate(a))
