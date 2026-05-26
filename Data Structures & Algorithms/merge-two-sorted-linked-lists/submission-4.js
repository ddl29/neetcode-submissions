/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        if (list1 === null)
            return list2;
        else if (list2 === null)
            return list1;

        let a = list1;
        let b = list2;
        
        let head;
        if (a.val < b.val) {
            head = a;
            a = a.next;
        } else {
            head = b;
            b = b.next
        }
        let headRef = head; 

        while (a !== null && b !== null) {
            if (a.val < b.val) {
                head.next = a;
                a = a.next;
            }
            else {
                head.next = b;
                b = b.next;
            }
            head = head.next;
        }

        if (a === null)
            head.next = b;
        else if (b === null)
            head.next = a;
        
        return headRef;
    }
}
