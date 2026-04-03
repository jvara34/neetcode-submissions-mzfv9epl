class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create hashset 

        # loop through nums 
            # check if value from nums is NOT in hashset 
                # add new value to hashset 
            # check if value from nums is IN hashset 
                # return true -> contain duplicate 
        # return false -> no duplicate 
        # time complexity: O(n) 
            # Loops through array once 
        # Space complexity: O(n) 
            # has linear memory because of hashset 

        hashset = set() 

        for values in nums: 
            if values not in hashset:
                hashset.add(values)
            elif values in hashset:
                return True # contain duplicate 
        
        return False 

        