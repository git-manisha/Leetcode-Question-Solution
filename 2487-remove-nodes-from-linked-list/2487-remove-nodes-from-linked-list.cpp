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
    ListNode* removeNodes(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        head = reverseNode(head);
        ListNode* t1 = head;
        ListNode* t2 = nullptr;
        int maxNode = -1;
        while(t1){
            maxNode = max(maxNode,t1->val);
            if(t1->val < maxNode){
                t2->next = t1->next;
                ListNode* temp = t1;
                t1 =t1->next;
                delete(temp);
            }
            else{
                t2 = t1;
                t1 = t1->next;
            }
        }
        return reverseNode(head);
    }
};