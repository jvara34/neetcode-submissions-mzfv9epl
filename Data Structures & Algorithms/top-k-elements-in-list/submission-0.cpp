class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> occur;
        vector<vector<int>> freq(nums.size() + 1);  

        for (const auto& i : nums) {
            occur[i] = 1 + occur[i]; // adding +1 because count[n] is initially 0  
        }
        for (const auto& j: occur) {
            freq[j.second].push_back(j.first);
        }

        vector<int> output; 
        for (int i = freq.size() - 1; i > 0; i--) {
            for (int n: freq[i]) {
                output.push_back(n); // n is equal to freq[n] 
            }
            if (output.size() == k) {
                return output; 
            }
        }
        return output; 
    }
};
