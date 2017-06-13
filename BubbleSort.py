arr = map(int, raw_input().split(" "))

swap_needed = True
counter=0

while swap_needed == True:

	swap_needed = False
	
	for k in range(1,len(arr)-counter):
		if arr[k] < arr[k-1]:
			swap = arr[k]
			arr[k] = arr[k-1]
			arr[k-1] = swap	
			swap_needed = True
	counter+=1

print arr
