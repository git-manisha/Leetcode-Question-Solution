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
        int len =1;
        ListNode* temp = head;
        while(temp){
            temp = temp->next;
            len++;
        }
        int pos = len-n;
        ListNode* prev = nullptr;
        temp = head;
        while(pos>1){
            prev = temp;
            temp = temp->next;
            pos--;
        }
        if(prev == nullptr){
            head = temp->next;
        }
        else{
            prev->next = temp->next;
        }
        delete(temp);
        return head;
    }
};