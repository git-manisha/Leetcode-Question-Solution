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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* list1 = l1;
        ListNode* list2 = l2;
        ListNode * ans = new ListNode(1);
        ListNode* curr = ans;
        int presum =0;
        while(list1 || list2){

            int sum = presum;
            if(list1){ 
                sum = sum + list1->val;
                list1 = list1->next;
            }
            if(list2){
                sum = sum + list2->val;
                list2 = list2->next;
            }

            ListNode* temp = new ListNode(sum%10);
            curr->next = temp;
            curr = curr->next;
            presum = sum/10;
            
        }
        
        while(presum>0){
            ListNode* temp = new ListNode(presum%10);
            curr->next = temp;
            curr = curr->next;
            presum = presum/10;
        }
        ans = ans->next;
        return ans;
    }
};