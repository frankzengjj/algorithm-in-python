def binarySearch(alist, target):
    mid = len(alist)//2

    if len(alist)==0:
        return None
    if(alist[mid]==target):
        return alist[mid]
    elif(alist[mid] < target):
        return binarySearch(alist[mid+1:], target)
    else:
        return binarySearch(alist[:mid-1], target)

li = [1,2,3,4,5,6,7,8]
print(binarySearch(li,70))