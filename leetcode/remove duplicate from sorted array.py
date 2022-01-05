class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[l] = nums[j]
                l +=1
        return l
