class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l=[]
        k=[]
        for i in nums:
            if i != 0:
                l.append(i)
            else:
                k.append(i)
        new =  l+k

        nums[:]= new
