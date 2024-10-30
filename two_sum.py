class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # taking a dictionary to store the indexs as the value
        dict = {}

        for i,value in enumerate(nums):
            diff = target-value
            if diff in dict:
                return [dict[diff],i]
            dict[value] = i
        return []
