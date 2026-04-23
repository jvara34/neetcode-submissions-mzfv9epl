class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force method? 
        # Loop through nums triple nested loop
            # First loop starts at first index 
                # second loop starts at second index 
                    # third loop starts at third index
                        # checks if triplet can be made 
                        # index to next value 

        # two pointer solution 
        # solution = [] 
        # sortednums = sort(nums) 
        # nested loop -> This is the ith value 
        # [-1,0,1,2,-1,-4]
        #   i L         R 
            # # sort nums
            # for i in range(len(nums)):
            #     skip duplicate i values
            #     L = i + 1, R = len(nums) - 1
            #     while L < R:
            #         if sum == 0: solution.append([num[i], num[L], num[R]])
                        # Right pointer move left 
                        # left pointer move right 
            #         if sum too big: Right pointer move left 
            #         if sum too small: Left pointer move right 

        solution = [] 
        sort = sorted(nums)
        for i in range(len(nums)): 
            if i > 0 and sort[i] == sort[i-1]:
                continue 
            left = i + 1 
            right = len(nums) - 1
            while left < right: 
                current_sum = sort[i] + sort[left] + sort[right]
                if current_sum == 0:
                    solution.append([sort[i], sort[left], sort[right]])
                    left += 1
                    right -= 1
                    while left < right and sort[left] == sort[left - 1]:
                        left += 1
                    while left < right and right < len(sort) - 1 and sort[right] == sort[right + 1]:
                        right -= 1
                    
                elif current_sum > 0: 
                    right -= 1
                elif current_sum < 0: 
                    left += 1

        return solution