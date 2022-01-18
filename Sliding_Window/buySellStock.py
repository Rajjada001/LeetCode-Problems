# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Use the Kadane's algorithm

def bestTime(a):
    l = res = 0
    profit = 0
    for i in range(1,len(a)):
        profit += a[i]-a[i-1]
        profit = max(0,profit)
        res = max(res, profit)

    return res



print(bestTime([7,1,5,3,6,4]))