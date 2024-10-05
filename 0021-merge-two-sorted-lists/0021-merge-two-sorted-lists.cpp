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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == NULL){
            return list2;
        }
        if(list2 == NULL){
            return list1;
        }
        ListNode* l1 = list1;
        ListNode* l2 = list2;
        ListNode* start = nullptr;
        ListNode* last = nullptr;
        if(l1->val <= l2->val){
            start = l1;
            last = l1;
            l1 = l1->next;
            last->next = nullptr;
        }
        else{
            start = l2;
            last = l2;
            l2 = l2->next;
            last->next = nullptr;
        }
        while(l1!=nullptr && l2!=nullptr){
            if(l1->val <= l2->val){
                last->next = l1;
                last = l1;
                l1 = l1->next;    
            }
            else{
                last->next = l2;
                last = l2;
                l2 = l2->next;
            }
            last->next = nullptr;
        }
        if(l1 != nullptr){
            last->next = l1;
        }
        if(l2 != nullptr){
            last->next = l2;
        }
        return start;
    }
};