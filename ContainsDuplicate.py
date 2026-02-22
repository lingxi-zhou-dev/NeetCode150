class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for n in nums:
            if n not in dictionary:
                dictionary[n] = 1
            else:
                dictionary[n] += 1
                return True
        return False