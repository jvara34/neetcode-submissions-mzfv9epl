class Solution {
public:
    bool isAnagram(string s, string t) {
        // check if same size first 
        if (s.length() != t.length()) {
            return false; 
        }

        unordered_map<char, int> countS; // Created 2 hash maps for each string 
        unordered_map<char, int> countT; 
        for (int i = 0; i < s.length(); i++) { // Populating the 2 maps 
            countS[s[i]]++;
            countT[t[i]]++; 
        }
        return countS == countT; // either returns true or false based if both strings match 
    }
};
