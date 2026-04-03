class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Given two strings 
        # s = 'cat', t = 'tac' 
        # initialize hashmap 
        hashmap_1 = {} 
        hashmap_2 = {} 
        for values in s: 
            hashmap_1[values] = hashmap_1.get(values, 0) + 1
            
        for values in t: 
            hashmap_2[values] = hashmap_2.get(values, 0) + 1


        print(hashmap_1)
        print(hashmap_2)
        if hashmap_1 == hashmap_2: 
            return True 
        else: 
            return False

