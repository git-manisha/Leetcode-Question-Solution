/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> ans(m,vector<int> (n));
        ListNode *p = head;
        int top =0;
        int down = m-1;
        int left =0;
        int right = n-1;
        int dir=0;
        if(!p){
            return {{}};
        }
        while(p){
            if(dir==0){
                for(int i=left;i<=right;i++){
                    if(p){
                    ans[top][i] = p->val;
                    p = p->next;
                    }
                    else{
                        ans[top][i] = -1;
                    }
                }
                top++;
            }
            if(dir==1){
                for(int i=top;i<=down;i++){
                    ans[i][right] = p->val;
                    p = p->next;
                }
                right--;
            }
            if(dir==2){
                for(int i= right;i>=left;i--){
                    ans[down][i] = p->val;
                    p = p->next;
                }
                down--;
            }
            if(dir==3){
                for(int i=down;i>=top;i--){
                    ans[i][left] = p->val;
                    p=p->next;
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