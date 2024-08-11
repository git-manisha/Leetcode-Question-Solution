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
        vector<ListNode*> ans;
        ListNode* temp = head;
        int len = 1;
        while(temp){
            temp = temp->next;
            len++;
        }
        int part = len/k;
        int rem =1;
        if(len>k){
        rem = len%k;
        }
        ListNode* curr = head;
        while(curr){
            int i = part;
            i = i + (rem>1?1:0);
            ListNode* t = curr;
            while(i>1 && curr->next){
                curr = curr->next;
                i--;
            }
            ListNode* p = curr;
            curr = curr->next;
            p->next = NULL;
            ans.push_back(t);
            k--;
            rem--;
        }
        while(k!=0){
            ans.push_back(NULL);
            k--;
        }
        return ans;
    }
};