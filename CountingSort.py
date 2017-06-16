arr = map(int, raw_input().split(" "))
maxi=arr[0]; mini=arr[0]

for i in arr:
	if i < mini:
		mini=i
	if i > maxi:
		maxi=i

count = [0 for _ in range(maxi+1)]

for i in arr:
	count[i]+=1

for i in range(1,len(count)):
	count[i]+=count[i-1]

output = [0 for _ in range(0,len(arr))]

for i in arr:
	output[count[i]-1]=i
	count[i]-=1

print output
