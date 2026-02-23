import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # cannot modify the input array because we need to keep track of the original index.
        left = 0
        right = len(nums) - 1

        while right >= left:
            middle = left + (right - left)//2

            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle

        return -1