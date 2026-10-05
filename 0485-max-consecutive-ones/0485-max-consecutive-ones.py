class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxi=0
        maxcount=0
        for i in nums:
            if i ==1:
                maxi+=1
                maxcount = max(maxcount,maxi)
            else:
                maxi=0
        return maxcount
