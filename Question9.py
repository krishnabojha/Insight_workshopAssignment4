########### find the number in list
def binary_search(arr,r,l,x):
    if l>=r:
        mid=r+(l-r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,r,mid-1,x)
        else:
            return binary_search(arr,mid+1,l,x)
    else:
        return -1
    
arr = [ 2, 3, 10, 40, 5, 9,1]
arr.sort()
x=int(input('Enter number : '))
# x =int(input('Enter a number : '))
result = binary_search(arr,0,len(arr)-1, x) 
print('input array : ',arr)
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")