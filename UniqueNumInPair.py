def UniqueNumber(a):
    count = 0
    for i in a:
        count = count ^ i
    return count


a = [1,1,2,2,3,4,4,5,5]
print(UniqueNumber(a))