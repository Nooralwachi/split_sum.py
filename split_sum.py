def split_sum(nums):
	l=0
	r=-1

	left=nums[:l+1]
	right=nums[r:]
	
	
	flag= True
	while(flag):
		if sum(left)==sum(right):
			flag =False
			print(left, right)
		elif sum(left)>sum(right):
			r -=1
			right = nums[r:]
			# print(right)
		else:
			l +=1
			left = nums[:l+1]
			# print(left)
			





split_sum([4, 6, 8, 2])
