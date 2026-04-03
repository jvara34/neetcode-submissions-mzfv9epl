class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap -> key is values from list, index are values 
        x = {} 
        # fill hashmap 
        for i in range(len(nums)): 
            x[nums[i]] = i # filling hashmap with value is the key 

        for j, n in enumerate(nums):
        # j is index, n is value at specific index j
        # diff -> want to compare to the hashmap (keys) 
            diff = target - n
            # Diff = 7 - 3 -> 4 
            # diff cannot be the same as current index j 
            if diff in x and x[diff] != j:
                return [j, x[diff]]

            # is same value on the same index 
            # n = 3 j = 0
            # [3:0, 4:1, 5:2, 6:3]
            # [Key: value]
            # x[4] = 1 