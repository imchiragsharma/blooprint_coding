class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #we have to return number of element which is not equal to val and also change nums

        k = 0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k += 1
        return k