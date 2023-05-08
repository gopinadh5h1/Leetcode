class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int,int>freq;
        int ans=0;
        for(auto it:nums){
            int b = k - it;
            if(freq[b]>0){
                ans++;
                freq[b]--;
            }
            else{
                freq[it]++;
            }
        }
        return ans;
        
    }
};