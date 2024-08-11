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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*> ans(k,NULL);
        ListNode* temp = head;
        int len = 0;
        while(temp){
            temp = temp->next;
            len++;
        }
        int part = len/k;
        int extraNode = len%k;
        ListNode* curr = head;
        ListNode* prev = nullptr;
        for(int i=0;i<k;i++){
            ans[i] = curr;
            for(int count=1;count<=part + (extraNode>0?1:0);count++){
                prev = curr;
                curr = curr->next;
            }
            if(prev)
                prev->next = NULL;
            extraNode--;
        }
        return ans;
    }
};