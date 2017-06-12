def QuickSort(arr,left,right):
	if (left>=right) == False:
		pivot = arr[(left+right)/2]
		index = Partition(arr,left,right,pivot)
		QuickSort(arr,left,index-1)
		QuickSort(arr,index,right)

def Partition(arr,left,right,pivot):
	while left <= right:
		while arr[left] < pivot:
			left+=1
		while arr[right] > pivot:
			right-=1
		if left <= right:
			swap = arr[left]
			arr[left] = arr[right]
			arr[right] = swap
			left+=1;right-=1

	return left
	

arr = map(int, raw_input().split(" "))
QuickSort(arr,0,len(arr)-1)

print arr
