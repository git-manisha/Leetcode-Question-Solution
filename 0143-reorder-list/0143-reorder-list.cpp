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
    ListNode * reverseNode(ListNode* head){
        ListNode* t1 = head;
        ListNode* prev = nullptr;
        ListNode* last = nullptr;

        while(t1){
            last = prev;
            prev = t1;
            t1 = t1->next;
            prev->next = last;
        }
        return prev;
    }
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        

        ListNode* rev = reverseNode(slow);
        ListNode* first = head;
        ListNode* second = nullptr;
        ListNode* temprev = nullptr;
        
        while(rev->next != nullptr){
                temprev = rev->next;
                second = first->next;
                first->next = rev;
                rev->next = second;
                first = second;
                rev = temprev;
        }
    }
};