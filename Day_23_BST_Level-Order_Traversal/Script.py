import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = []
        queue.append(root)
        while len(queue)!=0:
            temp_node = queue.pop(0)
            print (temp_node.data,end=' ')
            if temp_node.left is not None:
                queue.append(temp_node.left)
            if temp_node.right is not None:
                queue.append(temp_node.right)
            

        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
