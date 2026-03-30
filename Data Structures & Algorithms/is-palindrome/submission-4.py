class Solution:
    def isPalindrome(self, s: str) -> bool:
        # only read the alphanumeric chars specical characters and spaces don't count 
        # Order matters, all lower, 
        # .isalnum() -> return true if only letters, return false if special char or space 
        # s.lower() for all letters to be lower case 

        l = 0 
        r = len(s) - 1
        S = s.lower()
        while l < r: 
            if not S[l].isalnum(): 
                l += 1
                continue 
            elif not S[r].isalnum():
                r -= 1
                continue 
            
            if S[l] == S[r]: 
                r -= 1
                l += 1
            else: 
                return False 
        return True
                
        



        '''
        ['Was it a car or a cat I saw?']
          ^                         ^ 
          (l)                      (r)
        if (left) s[0].isalnum 
            true -> s[0] = w
        if (right) s[n-1].isalnum
            s[n-1] = 'w' -> true 
            r -= 1


        while l < r 
            first check -> is it a letter? 
               if (left) s[0].isalnum 
                    true -> s[0] = w
                if (right) s[n-1].isalnum
                    s[n-1] = 'w' -> true 
                    r -= 1
            
            while first check and second check are true: (second check)
                if s[0] === s[n-1]
                    continue 
                else: 
                    return false 
            return true 
            



        first check -> is it a letter? 
        second check -> is that letter the same as the left and right? 


        '''
