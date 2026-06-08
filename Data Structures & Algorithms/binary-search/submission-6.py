class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Use BST to find the element. 
        # Create three pointers left and right and middle 
        # Middle = (left+ right) // 2 the two '//' means round to the floor. 
        # Brute force would be to check every element in the array. Time complexity O(n) which is slower than O(lgn)
        left = 0 
        right = len(nums) - 1
        middle = left + (right - left) // 2

        while left <= right:
            if nums[middle] == target:
                return middle 
            elif nums[middle] > target: 
                right = middle - 1
                middle = left + (right - left) // 2
            elif nums[middle] < target:
                left = middle + 1
                middle = left + (right - left) // 2
        return -1 