class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force solution (Not optimal) 
            # Nest for loop 
                # Current position 
                    # Multiple every position except current position 
        # Time complexity O(n^2) 
        # Space complexity O(n) 
        # nums = [1,2,4,6]
        # Prefix and Suffix? 
        # prefix = [] This hold the values in the array from the left of the current value 
        # index = [0, 1, 2, 3]
        # predix = [[1], [1], [1,2], [1,2,4]]
        # suffix = [[2,4,6], [4,6], [6], [0]]

        # at index [0] 
            # prefix [1] * suffix[2,4,6]
            # 0 + 48 
            # sol = append

        # If prefix[0] = 1, how would you calculate prefix[1]? And then prefix[2]?
            # if i != currentIndex 
                #product *= prefix[i]
        prefix = [1] 
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])

        suffix = []
        for i in range(len(nums), 0, -1):
            # So starting from the top down 
            # first [ , , , 1]
            #               <- 
            if i == len(nums): 
                suffix.append(1)
                continue
            suffix.insert(0, suffix[0] * nums[i])
        sol = []
        for i in range(len(nums)):
            sol.append(prefix[i] * suffix[i])
        
            
        return sol
            