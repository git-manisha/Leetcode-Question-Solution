class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int n = matrix[0].size();
        int top = 0;
        int down = matrix.size()-1;
        int l = 0;
        int r = matrix[0].size()-1;
        int dir =0;
        while(top<=down && l<=r){
            if(dir==0){
                for(int i=l;i<=r;i++){
                    ans.push_back(matrix[top][i]);
                }
                top++;
            }
            if(dir==1){
               for(int j=top;j<=down;j++){
                ans.push_back(matrix[j][r]);
                }
                r--;
            }
            if(dir == 2){
                for(int t=r;t>=l;t--){
                    ans.push_back(matrix[down][t]);
                }
                down--;
            }
            if(dir == 3){
                for(int s=down;s>=top;s--){
                    ans.push_back(matrix[s][l]);
                }
                l++;
            }
            dir++;
            if(dir==4){
                dir =0;
            }
        }
        return ans;
    }
};