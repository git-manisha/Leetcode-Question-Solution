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
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* p = nullptr;
        ListNode* q = nullptr;
        while(fast && fast->next){
            p=q;
            q = slow;
            slow = slow->next;
            fast = fast->next->next;
            q->next = p;
        }
        int maximum = -1;
        while(q && slow){
            maximum = max(maximum,q->val+slow->val);
            q = q->next;
            slow = slow->next;
        }
        return maximum;
    }
};