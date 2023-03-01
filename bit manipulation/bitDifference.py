class Solution:
    def countBitsFlip(self,a,b):
        num = a^b
        res = 0
        while num:
            num = num&(num-1)
            res +=1
        return res
