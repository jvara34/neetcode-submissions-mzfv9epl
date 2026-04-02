class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap
        hashmap = {} 
        #loop through each string
        for cur in strs: 
            #sort the current_string
            sort_string = ''.join(sorted(cur)) # = act
                #if sorted string is already a key in the hashmap
            if sort_string in hashmap: 
                    # 'in' checks the keys  
                    # 'act' -> key 
                    #hashmap[key].append(current_string)
                hashmap[sort_string].append(cur)   
                #else
            else: 
                hashmap[sort_string] = [cur]
                    #hashmap[key] = [current_string]
        #solution = []
        solution = [] 
        #loop through the values of hashmap
        for value in hashmap.values(): 
            solution.append(value) 
            #append value to the solution
        return solution




        ['ca','cat','tea', 'cannot']
        m=4 
        n =6