class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if(p.length() > s.length())
        {
            return result;
        }
        vector<int> pmp(26,0);
        vector<int> smp(26,0);
        for(int i=0;i<p.length();i++)
        {
            char ch = p[i];
            pmp[ch - 'a']++;
        }
        int n = p.length()-1;
        char c;
        for(int j=0;j<n;j++)
        {
            c = s[j];
            smp[c - 'a']++;   
        }

        int k=0;
        for(int i=n;i<s.size();i++)
        {
            c = s[i];
            smp[c - 'a']++;
            if(smp == pmp)
            {
                result.push_back(k);
            }
            smp[s[k]-'a']--;
            k++;
        }

        return result;
    }
};