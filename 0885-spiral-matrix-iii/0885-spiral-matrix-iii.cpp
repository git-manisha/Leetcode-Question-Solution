class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        vector<vector<int>> direction{
                                    {0,1},//East
                                    {1,0}, //South
                                    {0,-1}, //West
                                    {-1,0} //north
                                };
        vector<vector<int>> ans;
        int step=0;
        ans.push_back({rStart,cStart});
        int r = rStart;
        int c = cStart;
        int dir=0;
        while(ans.size() < rows*cols){
            if(dir==0 || dir==2){
                step++;
            }
            for(int count=0;count<step;count++){
                rStart +=direction[dir][0];
                cStart +=direction[dir][1];

                if(rStart >=0 && rStart<rows && cStart>=0 && cStart<cols){
                    ans.push_back({rStart,cStart});
                }
            }
            dir = (dir+1)%4;
        }
        return ans;
    }
};