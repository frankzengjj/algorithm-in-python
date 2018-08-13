def quick_sort(alist):
	quick_sort_helper(alist, 0, len(alist)-1)
	

def quick_sort_helper(alist,first,last):
	if first < last:
		split = partition(alist, first, last)
		quick_sort_helper(alist, first, split-1)
		quick_sort_helper(alist, split+1, last)

def partition(alist, first, last):
	pivot = alist[first]
	left = first+1
	right = last

	sortDone = False
	while not sortDone:
		while left <= right and alist[left] <= pivot:
			left = left + 1
		
		while alist[right] >= pivot and right >= left:
			right = right - 1

		if right < left:
			sortDone = True
		else:
			alist[left], alist[right] = alist[right], alist[left]

	alist[first], alist[right] = alist[right], alist[first]

	return right


ali = [54,26,93,17,77,31,44,55,20]
quick_sort(ali)
print(ali)