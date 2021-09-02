# from os import truncate
# from typing import SupportsRound


# class Solution:
#     def removeComments(self, source: list) -> list:
#         retlst=[]
#         multiFlag=False
#         retcode=""
#         idx1=-2
#         idx2=-2
#         same=False
#         for i in range(len(source)):
#             same=False
            
#             # if "/*" in source[i] or "*/" in source[i]:
#             #     print("branch 2")
#             #     retcode=""
#             #     idx1=-2
#             #     idx2=-2
#             retcode=source[i]
#             if "//" in source[i] and multiFlag==False:
                
#                 print("branch 1")
#                 idx=source[i].find("//")
#                 code=source[i][:idx]
#                 if code=="" or idx==0:
#                     print("branch 1.1")
#                     pass
#                 else:
#                     print("branch 1.2")
#                     retcode=code
                
#             if "/*" in source[i] and multiFlag==False:
#                 print("branch 2.1")

#                 idx1=source[i].find("/*")
#                 print(idx1,"idx1")

#                 code=source[i][:idx1]
#                 if  idx1==0:
#                     print("branch 2.1.1")
#                     pass
#                 else:
#                     print("branch 2.1.2")
#                     retlst.append(code)
#                 multiFlag=True
#                 same=True
#             if "*/" in source[i] and multiFlag==True:
#                 print("branch 2.2")
#                 if same==True:
#                     idx2=source[i].find("*/",idx1+2)
#                 else:
#                     idx1=-2
#                     idx2=source[i].find("*/",idx1+2)
#                 print(idx1,idx2, len(source[i]),"idx2 sourceLen")
#                 code=source[i][idx2+2:]
#                 if idx2==len(source[i])-2:
#                     print("branch 2.2.1")
#                     pass
#                 else:
#                     print("branch 2.2.2")
#                     retcode=code
                
#                 if retcode!="":
#                     print("branch 2.3")
#                     print("retcode", retcode)
#                     retlst[len(retlst)-1]+=retcode
#                 multiFlag=False
#                 idx1=-2
#                 idx2=-2
#                 retcode=""
#             elif multiFlag==True:
#                 print("branch 3")
#                 pass
#             else:
#                 print("branch 4")
#                 retlst.append(source[i])
#         return retlst
#     def singleComment(self, item:str)->bool:
#         striped=item.strip(" ")
#         if len(striped)>=2:
#             if "//" in striped:
#                 return True
#         return False
    
#     def multiLine(self, item:str)->bool:
#         striped=item.strip(" ")
#         if len(striped)>=2:
#             if "/*" in striped:
#                 return True
#         return False






#need to consider "a /* asd */ asdf /* asd */ asdfsd /* asd */"
#consider internal loop within each item in source
class Solution:
    def removeComments(self, source: list) -> list:
        multi=False
              
        multiSum=""
        retLst=[]
        for i in range(len(source)):
            retItem=source[i]
            head=source[i].find("/*")
            tail=source[i].find("*/")
            single=source[i].find('//')
            if multi==False:
                if head>=0 and single>=0:
                    if single<head-1:
                        retItem=retItem[:single]
                        
                    else:
                        if tail>head+1:
                            retItem=retItem[:head]+retItem[tail+2:]
                            retLst.append(retItem)
                            multi=False
                        else:
                            retItem=retItem[:head]
                            multi=True
                            multiSum+=retItem
                elif head>0:
                    if tail>head+1:
                        retItem=retItem[:head]+retItem[tail+2:]
                        retLst.append(retItem)
                        multi=False
                    else:
                        retItem=retItem[:head]
                        multi=True
                        multiSum+=retItem
                elif single>0:
                    retItem=retItem[:single]
                    retLst.append(retItem)
                else:
                    retLst.append(retItem)
            else:
                if tail>0:
                    multiSum+=retItem[tail+2:]
                    retLst.append(multiSum)
                    multiSum=""
                    multi=False
                else:
                    retLst.append(retItem)

                    

            

a=Solution()
print(a.removeComments(["a","b"]))