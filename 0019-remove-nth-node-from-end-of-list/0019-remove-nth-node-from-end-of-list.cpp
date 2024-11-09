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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        while(n>0){
            temp = temp->next;
            n--;
        }
        if(temp == nullptr){
            return head->next;
        }
        ListNode* prev = head;
        while(temp->next){
            prev = prev->next;
            temp = temp->next;
        }
        ListNode* t = prev->next;
        if(prev->next){
        prev->next = t->next;
        }
        delete t;
        return head;
    }
};