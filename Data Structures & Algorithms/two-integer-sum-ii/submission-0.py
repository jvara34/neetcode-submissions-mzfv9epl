class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given a list [1,2,3,4]
        # Target = 3
        # only one valid solution 
        # variable less than target 
        
       # left 
       left = 0 
       # rigth 
       right = len(numbers) - 1
       
       # While left < right 
       while left < right: 
        # check the sum numbers[left] + numbers[right]
        sums = numbers[left] + numbers[right]
        if sums < target:
            left += 1
        elif sums > target: 
            right -= 1
        elif sums == target:
            sol = []
            sol.append(left+1)
            sol.append(right+1)
            return sol
            # if sum < target
                # left += 1 
            # elif sum > target 
                # right -= 1 
            # if sum == target 
                # return left + 1, right + 1 
            
        