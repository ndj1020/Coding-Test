class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        while head :
            if head.val == False :
                return True
            else :
                head.val = False
                head = node.next
        return False
    
    def makeLinkedList(self, listInput, pos):
        head = None
        returnNode = None 


        for i in range(len(listInput)):
            newNode = ListNode(listInput[i])
            if (i == 0):
                head = newNode
                tmp1 = newNode
            else:
                tmp2 = newNode
                tmp1.next = tmp2
                tmp1 = tmp2

            if (i == pos):
                returnNode = newNode
            
            newNode.next = returnNode

        return head
                





        



s = Solution()
inputList = [3,2,0,-4] 
pos = 1
andy = 1

head = s.makeLinkedList(listInput=inputList, pos=pos)
for i in range(1,10):
    print(head.val)
    head = head.next
print(s.hasCycle(head=head))