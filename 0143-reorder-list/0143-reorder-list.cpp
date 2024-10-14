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
    ListNode* reverseNode(ListNode* slow){
        ListNode* p = nullptr;
        ListNode* q = nullptr;
        ListNode* first = slow;
        while(first){
            p=q;
            q = first;
            first = first->next;
            q->next = p;
        }
        return q;
    }
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;
        while(fast && fast->next){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        //prev->next = nullptr;
        ListNode* rev = reverseNode(slow);
        ListNode* curr = head;
        while(rev->next){
            ListNode* temp = curr->next;
            ListNode* temprev = rev->next;
            curr->next = rev;
            rev->next = temp;
            curr = temp;
            rev = temprev;
        }
    }
};