# 
# remember to use dictionary and hash when necessary,
# do not think dictionary or hash is not practical

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gpdict={}
        for i in range(len(strs)):
            if tuple(sorted(strs[i])) in gpdict:

                gpdict[tuple(sorted(strs[i]))].append(strs[i])
            else:
                gpdict[tuple(sorted(strs[i]))]=[strs[i]]
        return gpdict.values()



# below is a running time exceeded example, which does not meet the running time
# requirement
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         setlst=[]
#         setlst.append(self.creatlst(strs[0]))
#         ctlst=[]
#         ctlst.append([strs[0]])
#         for i in range(1,len(strs)):
#             put=False
#             # miss=[]
#             for j in range(len(setlst)):
#                 newlst=setlst[j].copy()
#                 miss=[]
#                 if len(newlst)!=len(strs[i]):
#                     continue
#                 for k in range(len(strs[i])):
#                     if strs[i][k] in newlst:
#                         newlst.remove(strs[i][k])
#                     else:
#                         miss.append(strs[i])
#                         break
#                 if len(newlst)==0 and len(miss)==0:
#                     put=True
#                     ctlst[j].append(strs[i])
#                     break
#             if put==False:
#                 setlst.append(self.creatlst(strs[i]))
#                 ctlst.append([strs[i]])
#         return ctlst
#
#
#
#
#     def creatlst(self, s:str)->list():
#         ret=list(s)
#
#         return ret
#
