nums = map(int, raw_input().split(" "))

print nums

for i in range(1,len(nums)):
	cur_pos = i
	cur_elem = nums[cur_pos]
	shift_pos = cur_pos

	for j in range(i,0,-1):
		if cur_elem < nums[j-1]:
			shift_pos = j-1

	for k in range(cur_pos,shift_pos,-1):
		nums[k] = nums[k-1]

	nums[shift_pos] = cur_elem

print nums
