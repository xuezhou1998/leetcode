# # class Solution:
# #     def findAnagrams(self, s: str, p: str) -> List[int]:
# #         curr=0
# #         t=0
# #         ret=[]
# #         lst_p=list(p)
# #         # for i in range(len(s)):
# #         while True:
# #             # print(lst_p)
# #             if curr==len(s):
# #                 break
# #             else:
# #                 curr2=curr
# #                 p_lst=lst_p.copy()
# #                 while True:
                    
# #                     if len(p_lst)==0:
# #                         ret.append(curr)
# #                         break 
# #                     elif curr2>=len(s):
# #                         break
# #                     elif s[curr2] in p_lst:
# #                         p_lst.remove(s[curr2])
# #                         curr2+=1
# #                     elif s[curr2] not in p_lst:
# #                         break
                    
# #                     # print(p_lst)
                    
                        
# #                 curr+=1
# #         return ret

# # class Solution:
# #     def findAnagrams(self, s: str, p: str) -> List[int]:
# #         ctns=False
# #         ctns_idx=0
# #         curr=0
# #         p_lst_ori=list(p)
# #         ret=[]
# #         while True:
# #             if curr==len(s):
# #                 break
# #             else:
# #                 if ctns==False:
# #                     curr2=curr
# #                     p_lst=p_lst_ori.copy()
# #                     while True:
                        
# #                         if len(p_lst)==0:
# #                             ret.append(curr)
# #                             break 
# #                         elif curr2>=len(s):
# #                             break
# #                         elif s[curr2] in p_lst:
# #                             p_lst.remove(s[curr2])
# #                             curr2+=1
# #                         elif s[curr2] not in p_lst:
# #                             break
                    
# class Solution_old:
#     def findAnagrams(self, s: str, p: str) -> list[int]:
#         head=0
#         tail=0
#     def perm(self,avalst,slots:int)->set:
#         ret=set()
#         print(avalst)
#         avalstcp=avalst.copy()
#         for i in range(len(avalst)):
#             avalret=[]
#             if slots==1:
#                 if len(avalst)==1:
#                     avalret=avalst
#                 else:

#                     avalret=avalstcp.remove(avalst[i])
                
#             else:
#                 if len(avalst)==1:

#                     avalret=avalst
#                 else:

#                     avalret=self.perm(avalstcp.remove(avalst[i]),slots-1)
            
#             for j in range(len(avalret)):
                
#                 try:
#                     ret.add(avalst[i]+avalret[j])
#                 except:
#                     pass
#         return ret
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> list[int]:
#         h=0
#         t=0
#         mydict={}
#         currdict={}
#         ret=[]
#         for i in s:
#             if i not in mydict.keys():
#                 mydict[i]=0
#                 currdict[i]=0
#             else:
#                 mydict[i]+=1

#         while h<len(s):
            
            
#             if t==h:
#                 if s[t] in mydict.keys():
#                     currdict[i]+=1
#                     t+=1
#                 else:
#                     t+=1
#                     h+=1
#                     currdict=self.resetDict(currdict)
            
                
#             elif t-h+1<len(s):
#                 if s[t] in mydict.keys():
#                     if mydict[s[t]]>currdict[s[t]]:

#                         currdict[t]+=1
#                         t+=1
#                     else:
#                         currdict[s[h]]-=1
#                         h+=1
                        
#                         t+=1
                    
                    
#                 else:
#                     t+=1
#                     h=t
#                     currdict= self.resetDict(currdict)
#             else:
#                 if currdict==mydict:
#                     ret.append(h)
#                     currdict=self.resetDict(currdict)
#                     h=t
#                 else:
#                     currdict[s[h]]=0
#                     h+=1
                    

#     def resetDict(self, mydict:dict):
#         for i in mydict.keys():
#             mydict[i]=0
#         return mydict
    

        
# a=Solution()
# # print(a.perm(['1','s','3'],3))
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        h=0
        t=0
        mydict={}
        currdict={}
        ret=[]
        for i in p:
            if i not in mydict.keys():
                mydict[i]=1
                currdict[i]=0
            else:
                mydict[i]+=1
        # print('mydict:', mydict)

        while h<len(s) and t<=len(s):
            # print(currdict)
            # print(h,t)
            if t==len(s):
                if t-h<len(p):
                    pass
                else:
                    # print(currdict==mydict)
                    # print(currdict,mydict)
                    if currdict==mydict:
                        ret.append(h)
                        # currdict=self.resetDict(currdict)
                        # h=t
                        currdict[s[h]]-=1
                        h+=1

                        # t+=1
                        # print(6)
                    else:
                        currdict[s[h]]-=1
                        h+=1
                        # print(7)
                break
            elif t==h:
                if s[t] in mydict.keys():
                    currdict[s[t]]+=1
                    t+=1
                    # print(1)
                else:
                    t+=1
                    h+=1
                    currdict=self.resetDict(currdict)
                    print(2)
                
            elif t-h<len(p):
                if s[t] in mydict.keys():
                    if mydict[s[t]]>currdict[s[t]]:

                        currdict[s[t]]+=1
                        t+=1
                        print(3)
                    else:
                        currdict[s[h]]-=1
                        currdict[s[t]]+=1
                        h+=1
                        
                        t+=1
                        print(4)
                    
                    
                else:
                    t+=1
                    h=t
                    currdict= self.resetDict(currdict)
                    print(5)
            else:
                # print(currdict==mydict)
                print(currdict,mydict)
                if currdict==mydict:
                    ret.append(h)
                    # currdict=self.resetDict(currdict)
                    # h=t
                    currdict[s[h]]-=1
                    h+=1
                        
                    # t+=1
                    print(6)
                else:
                    currdict[s[h]]-=1
                    h+=1
                    print(7)
        return ret

    def resetDict(self, mydict:dict):
        for i in mydict.keys():
            mydict[i]=0
        return mydict