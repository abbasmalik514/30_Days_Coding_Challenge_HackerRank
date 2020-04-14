# Finding Height of a BST

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

    def heightFinder(self,node,height):
        left_height=0
        right_height=0
        if node.left is not None:
            left_height=self.heightFinder(node.left,height+1)
        if node.right is not None:
            right_height = self.heightFinder(node.right,height+1)
        if height<left_height:
            height=left_height
        if height<right_height:
            height=right_height
        return height
   
    def getHeight(self,root):
        return self.heightFinder(root,0)        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
