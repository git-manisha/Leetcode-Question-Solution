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
    ListNode* reverseTo(ListNode* first){
        ListNode* p = nullptr;
        ListNode* q = nullptr;
        ListNode* temp = first;
        while(temp != nullptr){
            p=q;
            q=temp;
            temp = temp->next;
            q->next = p;
        }
        return q;
    }
    bool isPalindrome(ListNode* head) {
        if(head== nullptr || head->next == nullptr){
            return  true;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;
        while(fast!= nullptr && fast->next!= nullptr){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        prev->next = nullptr;
        ListNode* last = reverseTo(slow);
        ListNode* curr = head;
        while(curr!=nullptr && last!=nullptr){
            if(curr->val != last->val){
                return false;
            }
            curr = curr->next;
            last = last->next;
        }
        return true;
    }
};