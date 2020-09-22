"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Google:

Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

Example: 
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
"""

# solution
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)
    
    # Iterative solution
    def reverseIteratively(self, head):
        node1 = self
        cont = 0
        while node1 != None:
            node1 = node1.next
            cont += 1

        for i in range(cont - 1)[::-1]:
            node1 = self
            for j in range(i):
                #print(j, end ="")
                node1 = node1.next
            node2 = node1.next
            node2.next = node1
            node1.next = None
            #print(" -- " + str(node2.val), ", i = " + str(i))

    # Recursive solution:
    def reverseRecursively(self, head):
        
        if head.next.next != None:
            self.reverseRecursively(head.next)
        node = head.next
        node.next = head
        head.next = None

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()

#testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
