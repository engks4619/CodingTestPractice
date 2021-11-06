from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp_left = [1]
        temp_right = [1]
        result = []
        for i in range(len(nums)-1):
            temp_left.append(temp_left[-1] * nums[i])
            temp_right.append(temp_right[-1] * nums[len(nums)-1-i])
        for i in range(len(nums)):
            result.append(temp_left[i] * temp_right[len(nums)-1-i])
        return result

Solution.productExceptSelf("self",[1,2,3,4])