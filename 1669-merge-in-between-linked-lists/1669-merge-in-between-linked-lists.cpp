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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        
        int rm_element = b-a+1;
        ListNode* prev = nullptr;
        ListNode* curr = list1;
        int i=0;
        while(i<a && curr){
            prev = curr;
            curr = curr->next;
            i++;
        }
        while(rm_element>0){
            if(curr->next){
                prev->next = curr->next;
                ListNode* temp = curr;
                curr = curr->next;
                delete temp;
            }
            rm_element--;
        }
        ListNode* p = prev->next;
        prev->next = list2;
        prev = list2;
        while(prev->next){
            prev = prev->next;
        }
        prev->next = p;
        return list1;
    }
};