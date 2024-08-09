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
    ListNode* partition(ListNode* head, int x) {
        if(head == nullptr || head->next == nullptr){
            return head;
        }
        ListNode* small = new ListNode(0);
        ListNode* large = new ListNode(0);
        ListNode* smallp = small;
        ListNode* largep =large;
        while(head != nullptr){
            if(head->val < x){
                if(small->next == nullptr){
                    small->next = head;
                    smallp = small->next;

                }
                else{
                    smallp->next = head;
                    smallp = smallp->next;
                }
                head = head->next;
                 smallp->next = nullptr;
            }
            else{
                if(large->next == nullptr){
                    large->next = head;
                    largep = large->next;

                }
                else{
                    largep->next = head;
                    largep = largep->next;
                }
                head = head->next;
                largep->next = nullptr;
            }
        }
        ListNode* temp = small;
        while(temp->next){
            temp = temp->next;
        }
        temp->next = large->next;
        return small->next;
    }
};