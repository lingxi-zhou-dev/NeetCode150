class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map  = {}

        for index, value in enumerate(nums):
            if value in num_map:
                num_map[value].append(index)
            else:
                num_map[value] = [index]

        print(num_map)

        idx2 = 0

        for idx1, n1 in enumerate(nums):

            n2 = target - n1

            if n2 in num_map:
                # if n1 = n2, then n2 index has to be the second value with the key
                if n1 == n2 and len(num_map[n2]) > 1:
                    print("n1: ", n1, "n2: ", n2)
                    idx2 = num_map[n2][1]
                elif n1 == n2 and len(num_map[n2]) == 1:
                    continue
                else:
                    idx2 = num_map[n2][0]
                return [idx1, idx2]
            else:
                continue