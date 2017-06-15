import math

""" INSERTION SORT Method called by Buckets """
def InsertionSort(ele):
	
	for i in range(1,len(ele)):
		cur_pos = i
		cur_val = ele[cur_pos]
		shift_pos = cur_pos

		for j in range(i,0,-1):
			if cur_val < ele[j-1]:
				shift_pos = j-1

		for k in range(cur_pos,shift_pos,-1):
			ele[k]=ele[k-1]

		ele[shift_pos]=cur_val

	return ele


arr = map(int, raw_input().split(" "))
maxi = max(arr)
divider = math.ceil((maxi+1)/len(arr))

buckets = [list() for _ in range(10)]

for i in arr:
	buckets[int(math.floor(i/divider))].append(i)

while [] in buckets:
	buckets.remove([])

cntr=0
for i in buckets:
	i = InsertionSort(i)
	for j in i:
		arr[cntr]=j
		cntr+=1

print arr
