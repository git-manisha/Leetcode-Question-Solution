class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        long long n = grid[0].size();
        if(n==1){
            return 0;
        }
        long long min_sum = LLONG_MAX;
        long long i,j,x;
        long long pre_sum[2][n];
        pre_sum[0][0] = grid[0][0];
        for(i=1;i<n;i++){
            pre_sum[0][i] = grid[0][i]+pre_sum[0][i-1];
        }
        pre_sum[1][0] = grid[1][0];
        for(j=1;j<n;j++){
            pre_sum[1][j] = grid[1][j] + pre_sum[1][j-1];
        }
        min_sum = min(pre_sum[0][n-1]-pre_sum[0][0],pre_sum[1][n-2]);
        for(i=1;i<n-1;i++){
            long long cv = max(pre_sum[0][n-1]-pre_sum[0][i],pre_sum[1][i-1]);
            if(cv<min_sum){
                min_sum = cv;
            }
        }
        return min_sum;
    }
};