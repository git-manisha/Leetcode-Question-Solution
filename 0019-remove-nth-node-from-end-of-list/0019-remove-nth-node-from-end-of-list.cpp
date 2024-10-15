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
        ListNode* node = head;
        int countnode = 0;
        
        while(node){
            countnode++;
            node = node->next;
        }
        int x = countnode-n;
        ListNode* first = head;
        ListNode* prev = nullptr;
        while(x>0){
            prev = first;
            if(first){
            first = first->next;
            }
            x--;
        }
        if(prev == nullptr){
            head = first->next;
        }
        else{
            prev->next = first->next;
        }
        delete first;
        return head;
    }
};