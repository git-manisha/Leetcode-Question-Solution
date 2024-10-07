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
    ListNode* removeElements(ListNode* head, int val) {
        if(head == nullptr){
            return head;
        }
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while(curr){
            if(curr->val == val){
                if(prev){
                    prev->next = curr->next;
                }
                else{
                    head = curr->next;
                }
                ListNode* temp = curr;
                curr = curr->next;
                delete temp;
            }
            else{
                prev = curr;
                curr = curr->next;

            }
        }
        return head;
    }
};