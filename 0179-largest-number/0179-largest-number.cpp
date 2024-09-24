class Solution {
public:
    bool myCompetitor(string &s1,string &s2){
        if(s1+s2 > s2+s1){
            return true;
        }
        return false;
    }
    string largestNumber(vector<int>& nums) {
        vector<string> st;
        st.push_back(to_string(nums[0]));

        for(int i=1;i<nums.size();i++){
            st.push_back(to_string(nums[i]));

            int j = st.size()-1;
            while(j>0){
                if(myCompetitor(st[j],st[j-1])){
                    swap(st[j],st[j-1]);
                }
                else{
                    break;
                }
                j--;
            }
        }
        string result ="";
        for(int i=0;i<st.size();i++){
            result +=st[i];
        }
        return result;
    }
   
};