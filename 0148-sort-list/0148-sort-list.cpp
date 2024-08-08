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
    ListNode* sortList(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode* prev = head;
        while(prev){
            ListNode* second;
            if(prev->next != NULL){
                second = prev->next;
            }
            while(second){
                if(prev->val > second->val){
                    swap(prev->val,second->val);
                }
                second = second->next;
            }
            prev = prev->next;
        }
        return head;
    }
};