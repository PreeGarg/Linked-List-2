'''
Problem: Delete without head pointer
Time Complexity: O(1)
Space Complexity: O(1)
Did this code successfully run on Leetcode: Yes
Any problem you faced while coding this: No
Your code here along with comments explaining your approach:
        copied the curr node's next value to curr node
        and deleted the next node of the curr node
'''

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        temp = curr_node.next
        curr_node.data = temp.data
        curr_node.next = temp.next