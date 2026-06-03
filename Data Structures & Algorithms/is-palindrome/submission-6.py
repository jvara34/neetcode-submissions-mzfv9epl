class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string.isalnum() - > Checks if current char is a alpanumeric 
        # Two pointer solution saves on space complexity but same time complexity 
        # left starts at 0 
        left = 0 
        # right starts at end of string s 
        right = len(s) - 1 
        s = s.lower()
        #two pointer while left < right 
        while left < right: 
            if s[left].isalnum() and s[right].isalnum():
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                else: 
                    return False 
            if s[left].isalnum() == False:
                left += 1
            elif s[right].isalnum() == False:
                right -= 1
        
        return True 