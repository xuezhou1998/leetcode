# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def verticalTraversal(self, root: TreeNode) :
#         ret=[]
#         mydict={}
#         # mydict[0]=[root.val]
#         mydict=self.recsv(root,0,0,mydict)
        
#         for i in sorted(mydict.keys()):
#             ret.append(mydict[i])
#         return [[3,15],[9],[20],[7]]

#     def recsv_old(self, root: TreeNode, column:int,cdict:dict):
#         print(root.val, cdict)
#         if column in cdict:
#             cdict[column].append(root.val)
            
#         else:
#             cdict[column]=[root.val]
#         if root.right!=None:
#             cdict=self.recsv(root.right,column+1,cdict)
#         if root.left!=None:
            
#             cdict=self.recsv(root.left,column-1,cdict)
        
#         return cdict
#     def recsv(self,root:TreeNode, row:int,column:int,  cdict):
#         mykey= (row,column)
#         if mykey not in cdict.keys():
#             cdict[mykey]=[root.val]
#         else:
#             cdict[mykey]=sorted(cdict[mykey].append(root.val))
#         if root.left!=None:
#             cdict=self.recsv(root.left,row+1,column-1,cdict)
#         if root.right!=None:
#             cdict=self.recsv(root.right,row+1,column+1,cdict)
#         return cdict


# class Solution:
#     def verticalTraversal(self, root: TreeNode) :
#         ret=[]
#         mydict={}
#         # mydict[0]=[root.val]
#         mydict=self.recsv(root,0,0,mydict)
        
#         for i in sorted(mydict.keys()):
#             # sub_lst=[]
#             # for j in mydict[i].keys():
#             #     sub_lst.append(j)
            
#             ret.append(mydict[i])
#         return ret
#     def recsv(self, root:TreeNode, row:int,column:int,  cdict:dict):
#         mykey= column
#         if mykey not in cdict.keys():
#             cdict[mykey]=[]
#             cdict[mykey].append(root.val)
#         else:

#             cdict[mykey].append(root.val)
#             cdict[mykey]=sorted(cdict[mykey])
#         if root.left!=None:
#             cdict=self.recsv(root.left,row+1,column-1,cdict)
#         if root.right!=None:
#             cdict=self.recsv(root.right,row+1,column+1,cdict)
#         return cdict

class Solution:
    def verticalTraversal(self, root: TreeNode) :
        ret=[]
        mydict={}
        # mydict[0]=[root.val]
        mydict=self.recsv(root,0,0,mydict)
        curr=-99999
        sublst=[]
        print(mydict)
        # mylist=sorted(mydict.keys(),key=lambda l:l[1])
        mylist=sorted(mydict.keys(),key=lambda x: (x[1],x[0]))
        print(mylist)
        for i in range(len(mylist)):
            
            if mylist[i][1]>curr and curr==-999999:
                
                curr=mylist[i][1]
                for j in mydict[mylist[i]]:
                    sublst.append(j)
                if i==len(mylist)-1:
                    
                    ret.append(sublst)
                
            elif mylist[i][1]==curr:
                for j in mydict[mylist[i]]:
                    sublst.append(j)
                if i==len(mylist)-1:
                    
                    ret.append(sublst)
            
            else:
                # print(i,len(mylist)-1)
                if sublst!=[]:
                    ret.append(sublst)
                sublst=[]
                curr=mylist[i][1]
                for j in mydict[mylist[i]]:
                    sublst.append(j)
                if i==len(mylist)-1:
                    
                    ret.append(sublst)
            # print(i,ret,sublst)   
        return ret       
            # ret+=mydict[i]
#             if i==mylist[-1]:
#                 sublst+=mydict[i]
#                 ret.append(sublst)
#             elif i[1]<curr:
#                 print("error")
#                 exit(-1)
#             elif i[1]==curr:
#                 sublst+=mydict[i]
#             else:
                
#                 if sublst!=[]:
#                     ret.append(sublst)
#                     sublst=mydict[i]
#                 else:
#                     sublst=mydict[i]
            
            
            
            
        
    def recsv(self, root:TreeNode, row:int,column:int,  cdict:dict):
        mykey= (row,column)
        if mykey not in cdict.keys():
            cdict[mykey]=[]
            cdict[mykey].append(root.val)
        else:

            cdict[mykey].append(root.val)
            cdict[mykey]=sorted(cdict[mykey])
        if root.left!=None:
            cdict=self.recsv(root.left,row+1,column-1,cdict)
        if root.right!=None:
            cdict=self.recsv(root.right,row+1,column+1,cdict)
        return cdict


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.row=0
#         self.column=0

# class Solution:
#     def verticalTraversal(self, root: TreeNode) :
#         ret=[]
#         mydict={}
#         # mydict[0]=[root.val]
#         mydict=self.recsv(root,0,0,mydict)
        
#         for i in sorted(mydict.keys()):
#             ret+=mydict[i]
            
            
            
#         return ret
#     def recsv(self, root:TreeNode, row:int,column:int,  cdict:dict):
#         mykey= (row,column)
#         if mykey not in cdict.keys():
#             cdict[mykey]=[]
#             cdict[mykey].append(root.val)
#         else:

#             cdict[mykey].append(root.val)
#             cdict[mykey]=sorted(cdict[mykey])
#         if root.left!=None:
#             cdict=self.recsv(root.left,row+1,column-1,cdict)
#         if root.right!=None:
#             cdict=self.recsv(root.right,row+1,column+1,cdict)
#         return cdict



#     # def verticalTraversal(self, root: TreeNode) :
#     #     ret=[]
#     #     mydict={}
#     #     # mydict[0]=[root.val]
#     #     mydict=self.recsv(root,0,mydict)
#     #     sortedkeys=sorted(mydict.keys())
#     #     rw=sortedkeys[0][0]
#     #     for i in sortedkeys:
            
#     #         ret.append(mydict[i])
#     #     return ret

#     # def recsv(self, root:TreeNode, rc,cdict):
#     #     print(root.val, cdict)
#     #     if rc in cdict:
#     #         cdict[rc].append(root.val)
#     #         cdict[rc]=sorted (cdict[rc])
            
#     #     else:
#     #         cdict[rc]=[root.val]
#     #     if root.right!=None:
#     #         cdict=self.recsv(root.right,(rc[0]+1,rc[1]+1),cdict)
#     #     if root.left!=None:
            
#     #         cdict=self.recsv(root.left,(rc[0]+1,rc[1]-1),cdict)
        
#     #     return cdict
# # use a dict to record the vals for all columns, columns as keys, and list of vals as values,
# # each time create a new dict item or add to existing dict item
# # finally in the verticalTraversal, iterate the dict and add all items sequentially 