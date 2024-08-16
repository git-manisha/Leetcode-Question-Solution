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
    ListNode* mergeSort(ListNode* l1,ListNode* l2){
        if(!l1){ return l2; }
        if(!l2){ return l1; }
        ListNode* temp;
        ListNode* prev;
        if(l1->val < l2->val){
            temp = l1;
            prev = l1;
            l1 = l1->next;
        }
        else{
             temp = l2;
            prev = l2;
            l2 = l2->next;
        }
        while(l1!= NULL && l2!=NULL){
            if(l1->val < l2->val){
                prev->next = l1;
                l1 = l1->next;
                prev = prev->next;
            }
            else{
                prev->next = l2;
                l2 = l2->next;
                prev = prev->next;
            }
        }
        while(l1 != NULL){
            prev->next = l1;
            prev = prev->next;
            l1 = l1->next;
        }
        while(l2 != NULL){
            prev->next = l2;
            prev = prev->next;
            l2 = l2->next;
        }
        return temp;
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size()==0){
            return NULL;
        }
        ListNode* result = lists[0];
        for(int i =1;i<lists.size();i++){
            result = mergeSort(result,lists[i]);
        }
        return result;
    }
};