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
    ListNode* reverseList(ListNode* head) {
        ListNode* p = nullptr;
        ListNode* q = nullptr;
        ListNode* first = head;
        while(first!= nullptr){
            p = q;
            q = first;
            first = first->next;
            q->next = p;
        }
        head = q;
        return head;
    }
}; 