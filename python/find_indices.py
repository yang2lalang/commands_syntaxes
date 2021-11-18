#Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest such sequence).
#EXAMPLE
#       0  1  2  3  4   5   6  7   8  9  10  11  12  13
#Input: 1, 2, 4, 7, 10, 11, 7, 5, 12, 6, 7, 16, 18, 19
#Output: (3, 10)
#http://collabedit.com/jk6wt

def find_indices(arr=None):
    m = 0
    n = 0
    
    #find the location of the start of the sort start from 0
    for i in range(0,len(arr)):
        if arr[i] > arr[i+1]:
            m = i
            break
     #find the location of the start of the sort start from behind
    for i in range(len(arr)-1,0,-1):
        if arr[i] < arr[i-1]:
            n = i
            break
    #initialize smallest and largest
    largest = arr[m]
    smallest = arr[m]
    
    #In the unsorted sub array get the largest and smallest 
    for i in range(m,n):
        if arr[i] > largest:
            largest = arr[i] 
        if arr[i] < smallest:
            smallest = arr[i]

    #get indices m and n
    for i in range(0,m):
        if arr[i] > smallest:
            m = i
            break
    for i in range(len(arr)-1,n,-1):
        if arr[i] < largest:
            n = i
            break

    print(smallest,largest)
    return (m, n)
arrr = [1, 2, 4, 7, 10, 11, 7, 5, 12, 6, 7, 16, 18, 19]
print(find_indices(arrr))