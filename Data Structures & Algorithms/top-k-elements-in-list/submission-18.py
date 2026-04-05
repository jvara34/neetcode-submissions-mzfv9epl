class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap 
        hashmap = {} 
        freq = [] 

        for num in range(len(nums) + 1):
            freq.append([])
        
        # Fill hashmap with key, value 
        for num in nums: 
            hashmap[num] = 1 + hashmap.get(num, 0)
        # From hashmap
        for value, key in hashmap.items(): 
            freq[key].append(value)

        sol = [] 
        for i in range(len(freq) - 1, 0, -1): 
            for n in freq[i]:
                sol.append(n)
                if len(sol) == k:
                    return sol
            