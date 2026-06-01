class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        hashmap_s = {}
        hashmap_t = {}

        for i in s: 
            # key, value 
            hashmap_s[i] = hashmap_s.get(i, 0) + 1 # if no key in hashmap, value is 0 if key in hashmap value + 1
        for i in t: 
            # key, value 
            hashmap_t[i] = hashmap_t.get(i, 0) + 1
        # compare two hashmaps 
        if hashmap_s == hashmap_t:
            return True 
        else: 
            return False 