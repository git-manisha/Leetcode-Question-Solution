class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        vector<int> vc(26,0);
        for(int i=0;i<chars.length();i++){
            vc[chars[i]-'a']++;
        }
        int result =0;
        for(string &word : words){
            vector<int> temp(26,0);
            for(char &ch : word){
                temp[ch-'a']++;
            }
            bool ok = true;
            for(int i=0;i<26;i++){
                if(temp[i] > vc[i]){
                    ok = false;
                }
            }
            if(ok == true){
                result += word.length();
            }
        }
        return result;

    }
};