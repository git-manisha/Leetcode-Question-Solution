class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int,int> mp;

        for(int i=0;i<wall.size();i++){
            int sum=0;
            for(int j=0;j<wall[i].size()-1;j++){
                sum = sum+wall[i][j];
                mp[sum]++;
            }
        }
        int max_gap = 0;
        for(auto it:mp){
            if(max_gap < it.second){
                max_gap = it.second;
            }
        }
        return wall.size()-max_gap;
    }
};