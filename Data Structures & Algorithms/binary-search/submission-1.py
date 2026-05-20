class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # BST is already sorted in ascneding order 
        # Need to find targer variable 
        # Need to find target value within in nums
        # nums is the BST 
        # if exist return location in the BST (index)
        # Else return false 
       
        # left = 0 
        left = 0 
        # right = len(num) - 1
        right = len(nums) -1 
        # mid = (left + right) // 2
        mid = (left + right) // 2
        #                       // -> floor division so round down
        print("value of mid", nums[mid])
        # while left <= right:  Search the BST 
        while left <= right: 
            # check mid if is target 
            if nums[mid] == target: 
                # return mid 
                return mid
            # check if mid is greater than target
            if nums[mid] > target:  
                # Check left sub tree so update values 
                right = mid - 1
                mid = (left + right) // 2
                # right = mid - 1 don't need to re check mid 
                # mid = (left + right) // 2

            # Check if mid is less than target 
            if nums[mid] < target:
                # check right sub tree 
                # left = mid + 1 // don't need to recheck mid 
                left = mid + 1
                # mid = (left + right) // 2
                mid = (left + right) // 2



        return -1 
       