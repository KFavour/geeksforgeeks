def maxArea(A,le):
     #code here
    Area_max = 0
    for i in range(le):
        first = A[i]
        if A[i] > Area_max/(le-i) or A[i] <= Area_max/i:
            for j in range(i+1, le):
                second = A[j]
                if second > first:
                    Area = first*abs(i-j)
                else:
                    Area = second*abs(i-j)
                
                if Area > Area_max:
                    Area_max = Area
    return Area_max

Array = [41,24, 66, 30, 7, 91, 7, 37, 57, 87, 53, 83, 45, 9, 9, 58, 21, 88, 22, 46, 6, 30, 13, 68, 1, 91, 62, 55, 10, 59, 24, 37, 48, 83, 95, 41, 2,50, 91, 36, 74, 20]
enter = maxArea(Array, len(Array))
print(enter)
print(5**0.5)