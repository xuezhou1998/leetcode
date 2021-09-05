# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("start")
        def rec(root:"TreeNode",isp:bool,isq:bool):
            # print(root.val,isp,isq)
            a1=False
            a2=False
            
            if root.val==p.val:
                if isq==True:
                    
                    a1,a2,a3=True,True,root
                else:
                    l1,r1,l2,r2=False,False,False,False
                    if root.left!=None:
                        l1,r1,n=rec(root.left,True,False)
                    else:
                        l1,r1=isp,isq
                    if root.right!=None:
                        l2,r2,n=rec(root.right,True,False)
                    else:
                        l2,r2=isp,isq

                    if (l1 and r2) or (l2 and r1)or (l1 and r1) or (l2 and r2)== True:
                        a1,a2,a3= True,True,root
                    else:
                        if r1 or r2==True:
                            a1,a2,a3=True,True,root
                        else:
                            a1,a2,a3=True,(r1 or r2),None 
            elif root.val==q.val:
                if isp==True:
                    a1,a2,a3=True, True, root
                else:
                    l1,r1,l2,r2=False,False,False,False
                    if root.left!=None:
                        l1,r1,n=rec(root.left,False,True)
                    else:
                        l1,r1=isp,isq
                    if root.right!=None:
                        l2,r2,n=rec(root.right,False,True)
                    else:
                        l2,r2=isp,isq

                    if (l1 and r2) or (l2 and r1) or (l1 and r1) or (l2 and r2)== True:
                        a1,a2,a3=True,True,root
                    else:
                        if l1 or l2==True:  
                            a1,a2,a3=(l1 or l2),True,root
                        else:
                            a1,a2,a3=(l1 or l2),True,None
            else:
                l1,r1,l2,r2=False,False,False,False
                n1,n2=None,None
                if root.left!=None:
                    # print("s1")
                    l1,r1,n1=rec(root.left,False,False)
                else:
                    # print("s2")
                    l1,r1=isp,isq
                if root.right!=None:
                    # print("s3")
                    l2,r2,n2=rec(root.right,False,False)
                else:
                    # print("s4")
                    l2,r2=isp,isq

                if (l1 and r2) or (l2 and r1)or (l1 and r1) or (l2 and r2)== True:
                    # print("s5")
                    if n1!=None:
                        aa=n1
                    elif n2!=None:
                        aa=n2
                    else:
                        aa=root
                    a1,a2,a3= True,True,aa
                else:
                    # print("s6")
                    a1,a2,a3= (l1 or l2),(r1 or r2),None 
                
            # print("b",root,isp,isq)
            # print("bbb",root.val,a1,a2,a3)
            # if a1==True and a2==True:
            #     if 
            return a1,a2,a3
        res1,res2,n=rec(root,False,False)
        return n
            

            
                