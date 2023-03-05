'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.'''


def findMaxConsecutiveOnes(nums):
        sum = 0
        ones = []
        for i in range(len(nums)+1):
            if i==len(nums) or nums[i]!=1  :
                ones.append(sum)
                sum = 0
            else:
                sum += nums[i]
        return max(ones)
    
print(findMaxConsecutiveOnes([1,1,1,0,1,1,1])) #output :3
