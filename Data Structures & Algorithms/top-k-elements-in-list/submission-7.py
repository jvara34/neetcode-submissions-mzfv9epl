class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort version too complex break down for my understanding 
        count = {} 
        freq = [] # Need a list of the values 
        for i in range(len(nums) + 1): # need to be nums + 1 since it starts at 0 
            freq.append([]) 

        print(freq)

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1): #Starts at the end of the list to find the highest frequency. 
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res