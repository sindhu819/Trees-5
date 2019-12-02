'''
Leet code - 106 - populating next right pointer - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
time complexity - O(N) 
space - O(1)
Approach - level order traversal using BST without using queue

'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        level= root
        while (level!=None):
            curr=level
            while curr!=None:
                #case1 for 4 and 5
                if curr.left!=None:
                    curr.left.next=curr.right
                #case2 for 5 and 6
                if curr.right != None and curr.next != None:
                    curr.right.next=curr.next.left
                curr=curr.next
            level=level.left # 1 to 2
        return root
                    
