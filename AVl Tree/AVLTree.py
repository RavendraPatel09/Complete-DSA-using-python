class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.height=1
class AVL:
    def __init__(self):
        self.root=None
    def NodeHeight(self,p):
        hl=p.lchild.height if p and p.lchild else 0
        hr=p.rchild.height if p and p.rchild else 0
        return max(hl,hr)+1
    def BalanceFactor(self,p):
        hl=p.lchild.height if p and p.lchild else 0
        hr=p.rchild.height if p and p.rchild else 0
        return hl-hr
    def LLRotation(self,p):
        pl=p.lchild
        plr=pl.rchild
        pl.rchild=p
        p.lchild=plr
        p.height=self.NodeHeight(p)
        pl.height=self.NodeHeight(pl)
        if self.root==p:
            self.root=pl
        return pl
    def RRRotation(self,p):
        pr=p.rchild
        prl=pr.lchild
        pr.lchild=p
        p.rchild=prl
        p.height=self.NodeHeight(p)
        pr.height=self.NodeHeight(pr)
        if self.root==p:
            self.root=pr
        return pr
    def rInsert(self,p,key):
        if p is None:
            return Node(key)
        if key<p.data:
            p.lchild=self.rInsert(p.lchild,key)
        elif key>p.data:
            p.rchild=self.rInsert(p.rchild,key)
        p.height=self.NodeHeight(p)
        if self.BalanceFactor(p)==2 and self.BalanceFactor(p.lchild)==1:
            return self.LLRotation(p)
        if self.BalanceFactor(p)==-2 and self.BalanceFactor(p.rchild)==-1:
            return self.RRRotation(p)
        return p
    def Inorder(self,p):
        if p:
            self.Inorder(p.lchild)
            print(p.data,end=" ")
            self.Inorder(p.rchild)
tll=AVL()
tll.root=tll.rInsert(tll.root,30)
tll.root=tll.rInsert(tll.root,20)
tll.root=tll.rInsert(tll.root,10)
tll.Inorder(tll.root)
print()
trr=AVL()
trr.root=trr.rInsert(trr.root,10)
trr.root=trr.rInsert(trr.root,20)
trr.root=trr.rInsert(trr.root,30)
trr.Inorder(trr.root)