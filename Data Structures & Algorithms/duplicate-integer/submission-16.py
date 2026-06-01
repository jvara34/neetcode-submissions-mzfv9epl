class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashmap since it cannot have duplicate values (empty) 
    
    # Fill hashmap with values from array 'nums' 
    # Will hashmap return a True/False value if it has a duplicate? 
    # OR Compare the new hashmap with the nums and see if it has the same length. 
        # This is because hashmap won't have duplicates and then there is no dup so length is shorter 
        hashset = set() 
    # fill hashset with values from nums
        for i in nums: 
            hashset.add(i)
        # compare the hashset with nums 
        if len(hashset) == len(nums):
            return False 
        else: 
            return True 