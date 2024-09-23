class Solution {
public:
    int countPalindromicSubsequence(string s) {
        set<char> st;
        int count=0;
        for(int i=0;i<s.length();i++){
            st.insert(s[i]);
        }
        for(auto it:st){
            int i=0,j=s.length()-1;
            while(s[i] != it){
                i++;
            }
            while(s[j] != it){
                j--;
            }
            set<char> temp;
            if(i<j-1){
            for(int k=i+1;k<j;k++){
                temp.insert(s[k]);
            }
            }
            count = count + temp.size();

        }
        return count;
    }
};