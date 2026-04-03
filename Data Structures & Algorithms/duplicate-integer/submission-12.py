class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashset only carries unique values 
        # if a hashset has more than one unique value it returns false 
        # Create hashset 
        hashset = set()
        # fill hashset with nums
        for value in nums: # range(len(array)) -> index
            hashset.add(value)

        # just need to compare the len 
        if len(hashset) == len(nums):
            return False
        else:
            return True
            
            