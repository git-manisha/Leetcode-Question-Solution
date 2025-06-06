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
    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return true;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* p = nullptr;
        ListNode* q = nullptr;
        while(fast && fast->next){
            p = q;
            q = slow;
            slow = slow->next;
            fast = fast->next->next;
            q->next = p;
        }
        if(fast != nullptr){
            slow = slow->next;
        }
        while(q && slow){
            if(q->val != slow->val){
                return false;
            }
            q = q->next;
            slow = slow->next;
        }
        return true;
    }
};