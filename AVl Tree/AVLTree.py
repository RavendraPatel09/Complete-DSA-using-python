class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
        self.h=1
class AVL:
    def height(self,n):
        return n.h if n else 0
    def balance(self,n):
        return self.height(n.left)-self.height(n.right)
    def leftRotate(self,z):
        y=z.right
        z.right=y.left
        y.left=z
        z.h=max(self.height(z.left),self.height(z.right))+1
        y.h=max(self.height(y.left),self.height(y.right))+1
        return y
    def rightRotate(self,z):
        y=z.left
        z.left=y.right
        y.right=z
        z.h=max(self.height(z.left),self.height(z.right))+1
        y.h=max(self.height(y.left),self.height(y.right))+1
        return y
    def insert(self,root,key):
        if not root:
            return Node(key)
        if key<root.data:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        root.h=max(self.height(root.left),self.height(root.right))+1
        b=self.balance(root)
        if b>1:
            return self.rightRotate(root)
        if b<-1:
            return self.leftRotate(root)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
t=AVL()
root=None
for i in [30,20,10]:
    root=t.insert(root,i)
t.inorder(root)
