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
    ListNode* insertionSortList(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* curr = head;
        while(curr){
            ListNode* temp = curr->next;
            ListNode* alt = curr;
            while(temp){
                if(curr->val > temp->val){
                    alt->next = temp->next;
                    ListNode* t = temp;
                    temp = temp->next;
                    prev->next = t;
                    t->next = curr;
                    curr = t;
                }
                else{
                    alt = temp;
                    temp = temp->next;
                }
            }
            prev = prev->next;
            curr = curr->next;
        }
        return dummy->next;
    }
};