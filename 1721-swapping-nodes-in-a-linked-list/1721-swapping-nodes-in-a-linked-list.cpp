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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* temp = head;
        int len = 1;
        while(temp){
            temp = temp->next;
            len++;
        }
        int s = len-k;
        ListNode* s1 = head;
        ListNode* s2 = head;
        while(k>1){
            s1 = s1->next;
            k--;
        }
        while(s>1){
            s2 = s2->next;
            s--;
        }
        swap(s1->val,s2->val);
        return head;
    }
};