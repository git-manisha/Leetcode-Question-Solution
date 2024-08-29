class Solution {
public:
    bool valid(char ch){
        if((ch>='a' && ch<='z') || (ch>='0' && ch<='9') || (ch>='A' && ch<='Z')){
            return 1;
        }
            return 0;
    }
    char toLower(char ch){
        if((ch>='a' && ch<='z') || (ch>='0' && ch<='9')){
            return ch;
        }
        else{
        char chr = ch-'A'+'a';
        return chr;
        }
    }
    bool isPalindrome(string s) {
        string temp = "";
        for(int i=0;i<s.length();i++){
            if(valid(s[i])){
                temp += s[i];
            }
        }
        for(int i=0;i<temp.length();i++){
            temp[i] = toLower(temp[i]);
        }

        int i =0;
        int j = temp.length()-1;
        while(i<=j){
            if(temp[i] != temp[j]){
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
};