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
 /*
 This answer can be optimized lots probably
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int tempValue = l1->val+l2->val;
        bool carry=false;
        if (tempValue>=10){
            tempValue-=10;
            carry=true;
        }
        ListNode* answer = new ListNode(tempValue);
        ListNode* currentNode = answer;
        l1=l1->next;
        l2=l2->next;
        while(l1&&l2){
            ListNode* temp = nullptr;
            int value = 0;
            if((l1->val+l2->val)>=10){
                value+=(l1->val+l2->val-10);
                if(carry){
                    value+=+1;
                }
                carry = true;
            } else{
                value+=l1->val+l2->val;
                if(carry){
                    value+=+1;
                }
                if(value>=10){
                    value-=10;
                    carry=true;
                } else{
                    carry = false;
                }
            }
            temp = new ListNode(value);
            //temp->next=answer->next;
            //answer->next=temp;

            currentNode->next=temp;
            currentNode=temp;
            l1=l1->next;
            l2=l2->next;
        }
        //answer = answer->next;
        while(l1){
            ListNode* temp = nullptr;
            int value=l1->val;
            if(carry){
                value=l1->val+1;
            }
            if(value>=10){
                carry=true;
                value-=10;
            } else {
                carry = false;
            }
            temp = new ListNode(value);
            currentNode->next=temp;
            currentNode=temp;
            l1=l1->next;
        }
        while(l2){
            ListNode* temp = nullptr;
            int value=l2->val;
            if(carry){
                value=l2->val+1;
            }
            if(value>=10){
                carry=true;
                value-=10;
            } else {
                carry = false;
            }
            temp = new ListNode(value);
            currentNode->next=temp;
            currentNode=temp;
            l2=l2->next;
        }
        if(carry){
            currentNode->next= new ListNode(1);
        }
        return answer;
    }
};