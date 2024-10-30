class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #we will traverse the list from backward and check for the pivot element


        pivot = 0
        n = len(nums)

        for i in range(n-1,0,-1):
            if nums[i]> nums[i-1]:
                pivot = i
                break
        print(pivot)
        if pivot == 0:
            nums.sort()
            return 

        swap = n-1
        while nums[swap]<=nums[pivot-1]:
            swap -= 1

        nums[swap],nums[pivot-1] = nums[pivot-1],nums[swap]
        nums[pivot:] = sorted(nums[pivot:])
