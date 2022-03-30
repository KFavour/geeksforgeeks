#User function Template for python3

class Solution:
    def findMaxAverage(arr, n, k):
        # code here
        for index in range(n-k+1):
            if index == 0:
                Sum = sum(arr[index:index+k])
                Max_sum = [Sum, index]
            else:
                Sum += arr[index+k-1] - arr[index-1]
                if Sum > Max_sum[0]:
                    Max_sum = [Sum, index]
        
        return [Max_sum[1], Max_sum[0]]
    
    [xx, yy] = findMaxAverage([-469, -8, -358, -278, -214, -436, 400, -313], 8, 7)    
    print(xx, yy)