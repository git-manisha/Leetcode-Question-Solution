/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == NULL && headB == NULL){
            return 0;
        }
        ListNode* d1 = headA;
        ListNode* d2 = headB;
        int flag1 = 0;
        int flag2 =0;
        while(d1 || d2){
            if(d1 == d2){
                return d1;
            }
            d1 = d1->next;
            d2 = d2->next;
            if(d1==nullptr && d2==nullptr){
                return  0;
            }
            if(d1 == NULL){
                if(flag1 == 0){
                    d1 = headB;
                    flag1 = 1;
                }
                else{
                    d1 = headA;
                    flag1 = 0;
                }
            }
            if(d2 == NULL){
                if(flag2 == 0){
                    d2 = headA;
                    flag2 = 1;
                }
                else{
                    d2 = headB;
                    flag2 = 0;
                }
            }
        }
        return 0;
    }
};