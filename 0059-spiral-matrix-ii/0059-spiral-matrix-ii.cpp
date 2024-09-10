class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n,vector<int> (n));
        int top = 0;
        int down = n-1;
        int left = 0;
        int right = n-1;
        int dir = 0;
        int num = 1;
        int i=0;
        while(top<=down && left<=right){
            if(dir == 0){
                for(i=left;i<=right;i++){
                    ans[top][i] = num++;
                }
                top++;
            }
            if(dir == 1){
                for(i=top;i<=down;i++){
                    ans[i][right] = num++;
                }
                right--;
            }
            if(dir == 2){
                for(i=right;i>=left;i--){
                    ans[down][i] = num++;
                }
                down--;
            }
            if(dir == 3){
                for(i=down;i>=top;i--){
                    ans[i][left] = num++;
                }
                left++;
            }
            dir++;
            if(dir == 4){
                dir = 0;
            }
        }
        return ans;
    }
};