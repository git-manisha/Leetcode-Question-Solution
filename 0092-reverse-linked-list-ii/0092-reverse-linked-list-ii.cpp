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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode* dummy = new ListNode(-1);
        ListNode* prev = dummy;
        dummy->next = head;
        ListNode* curr = head;
        int i = right-left;
        while(left>1){
            prev =curr;
            curr = curr->next;
            left--;
        }
        while(i != 0){
            ListNode* temp = prev->next;
            prev->next = curr->next;
            curr->next = curr->next->next;
            prev->next->next = temp;
            i--;
        }
        return dummy->next;
    }
};