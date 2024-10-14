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
    void reorderList(ListNode* head) {
        stack<ListNode*> st;
        ListNode* p = head;
        while(p){
            st.push(p);
            p = p->next;
        }
        int size = st.size()/2;
        ListNode* curr = head;
        while(size>0){
            ListNode* temp = curr->next;
            curr->next = st.top();
            st.top()->next = temp;
            curr = temp;
            st.pop();
            size--;
        }
        curr->next = NULL;
    }
};