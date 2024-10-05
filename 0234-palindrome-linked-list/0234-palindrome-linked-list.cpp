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
    ListNode *reverselinkedlist(ListNode* head){
        if(!head || !head->next){
            return head;
        }
        ListNode *last = reverselinkedlist(head->next);
        head->next->next = head;
        head->next = NULL;
        return last;

    }
    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return true;
        }
         ListNode *s = head;
        ListNode *f = head;
        ListNode *prev = NULL;
        while(f && f->next){
            prev = s;
            s = s->next;
            f = f->next->next;
        }
        prev->next = NULL;
        ListNode *tail = reverselinkedlist(s);
        while(head != nullptr && tail != nullptr){
            if(head->val != tail->val){
                return false;
            }
            head = head->next;
            tail = tail->next;
        }
        return true;
    }
};