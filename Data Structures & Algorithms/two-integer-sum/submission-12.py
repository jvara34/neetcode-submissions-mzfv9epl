class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i  # value -> index

        for i in range(len(nums)):          # i is now an INDEX
            solution_value = target - nums[i]
            if solution_value in hashmap and hashmap[solution_value] != i:
                return [i, hashmap[solution_value]]

        return []