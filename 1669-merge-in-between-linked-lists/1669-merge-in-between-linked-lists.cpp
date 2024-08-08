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
        ListNode* t1 = list1;
        ListNode* temp = nullptr;
        int x = a;
        while(x>0){
            temp = t1;
            t1 = t1->next;
            x--;
        }
        int delNode = b-a+1;
        while(delNode >0){
            if(t1->next){
            temp->next = t1->next;
            delete t1;
            t1 = temp->next;
            }
            delNode--;
        }
        temp->next = list2;
        while(temp->next){
            temp = temp->next;
        }
        temp->next = t1;
        return list1;
    }
};