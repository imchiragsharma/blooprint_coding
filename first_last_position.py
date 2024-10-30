class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        first = self.first_element(nums,target,l,r)
        second = self.last_element(nums,target,l,r)
        return [first,second]

    #function to find first position of element
    def first_element(self,nums,target,l,r):
        res = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                res = mid
                r = mid-1 #if mid == target we decrease r to mid-1 to check if there is target on the left of mid
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid+1
        return res

    
    #function to find last postion of element
    def last_element(self,nums,target,l,r):
        res = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                res = mid
                l = mid + 1 #here we will check on the right side to mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return res
        