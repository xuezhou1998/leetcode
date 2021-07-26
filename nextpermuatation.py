
 
# # # Get all permutations of [1, 2, 3]

# # class Solution:
# #     def nextPermutation(self, nums: list) -> None:
# #         """
# #         Do not return anything, modify nums in-place instead.
# #         """
# #         # perm_sorted = sorted(list( permutations([1, 2, 3]))) 

# #         if nums==sorted(nums,reverse=True):
# #             for x in range(1,len(nums)):

# #                 extra=nums[0]
# #                 for i in range(len(nums)-x):
# #                     nums[i]=nums[i+1]
# #                 nums[-x]=extra
# #             return nums
# #         else:
# #             curr=-1
# #             curridx=-1
# #             for i in range(len(nums)-1,-1,-1):
# #                 if nums[i]>curr:
# #                     curr=nums[i]
# #                 else:
# #                     curridx=i
# #                     break
# #             print('current idx'+str(curridx))
# #             extra=nums[curridx]
# #             extra2=max(nums[curridx+1:]) 
# #             extra_idx=0
# #             for i in range(curridx+1,len(nums)):
# #                 # extra=min(nums[i:])
# #                 if nums[i]<extra2 and nums[i]>extra:
# #                     extra2=nums[i]
# #                     extra_idx=i
            
            
# #             nums[curridx]=extra2
# #             nums[extra_idx]=extra
# #             print(nums[:curridx+1],list(reversed(nums[curridx+1:])))
# #             nums=nums[:curridx+1]+list(reversed(nums[curridx+1:]))

# #             return nums 



        

# # a=Solution()
# # print(a.nextPermutation([5,4,3,2,1]))
# # print(a.nextPermutation([5,2,3,6,4,1]))


 
# # Get all permutations of [1, 2, 3]

# class Solution:
#     def nextPermutation(self, nums: list) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # perm_sorted = sorted(list( permutations([1, 2, 3]))) 
#         if len(nums)==1:
#             print('branch 1')
#             return nums
            
#         elif nums==sorted(nums,reverse=True):
#             for x in range(1,len(nums)):

#                 extra=nums[0]
#                 for i in range(len(nums)-x):
#                     nums[i]=nums[i+1]
#                 nums[-x]=extra
#             print('branch 2')
#             print(nums)
            
#         elif nums==sorted(nums):
#             if len(nums)==2:
#                 print('branch 3 1')
#                 nums=list(reversed(nums))
#             else:
#                 print('branch 3 2')
#                 # print(list(reversed(nums[len(nums)-2:])))
#                 # print(nums[:len(nums)-2])
#                 # part_a=nums[:len(nums)-2]
#                 # part_b=list(reversed(nums[len(nums)-2:]))
#                 # nums=part_a+part_b
#                 extra=nums[-1]
#                 nums[-1]=nums[-2]
#                 nums[-2]=extra
#                 print(nums)
#         else:
#             curr=-1
#             curridx=-1
#             for i in reversed(range(len(nums))):
#                 print(i)
#                 if nums[i]>curr:
#                     curr=nums[i]
#                 else:
#                     curridx=i
#                     break
            
            
#             print('current idx'+str(curridx))
#             extra=nums[curridx]
#             extra2=max(nums[curridx+1:]) 
#             extra_idx=0
#             for i in range(curridx+1,len(nums)):
#                 # extra=min(nums[i:])
#                 if nums[i]<extra2 and nums[i]>extra:
#                     extra2=nums[i]
#                     extra_idx=i
            
            
#             nums[curridx]=extra2
#             nums[extra_idx]=extra
#             print("nums 1",nums)
#             extra=101
#             for i in range(curridx+1,len(nums)):
#                 print("nums iter",nums)
#                 myMin=min(nums[i:])
#                 myMinIdx=nums[i:].index(myMin)+i
#                 extra=nums[i]
#                 nums[i]=myMin
#                 nums[myMinIdx]=extra

#                 # extra=nums[i]
#                 # nums[i]=myMin
                

                
                
#             # print(nums[:curridx+1],list(reversed(nums[curridx+1:])))
#             # nums=nums[:curridx+1]+list(reversed(nums[curridx+1:]))
#             print('branch 4')
#             print(nums)
# a=Solution()
# print(a.nextPermutation([5,4,3,2,1]))
# print(a.nextPermutation([5,2,3,6,4,1]))


        



class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # perm_sorted = sorted(list( permutations([1, 2, 3]))) 
        if len(nums)==1:
            print('branch 1')
            return nums
            
        elif nums==sorted(nums,reverse=True):
            for x in range(1,len(nums)):

                extra=nums[0]
                for i in range(len(nums)-x):
                    nums[i]=nums[i+1]
                nums[-x]=extra
            print('branch 2')
            print(nums)
            
        elif nums==sorted(nums):
            if len(nums)==2:
                print('branch 3 1')
                # nums=list(reversed(nums))
                extra=nums[0]
                nums[0]=nums[1]
                nums[1]=extra
            else:
                print('branch 3 2')
                # print(list(reversed(nums[len(nums)-2:])))
                # print(nums[:len(nums)-2])
                # part_a=nums[:len(nums)-2]
                # part_b=list(reversed(nums[len(nums)-2:]))
                # nums=part_a+part_b
                extra=nums[-1]
                nums[-1]=nums[-2]
                nums[-2]=extra
                print(nums)
        else:
            curr=-1
            curridx=-1
            for i in reversed(range(len(nums))):
                print(i)
                if nums[i]>=curr:
                    curr=nums[i]
                else:
                    curridx=i
                    break
            if curridx==len(nums)-2:
                extra=nums[len(nums)-1]
                nums[len(nums)-1]=nums[len(nums)-2]
                nums[len(nums)-2]=extra
            else:
                
            
                print('current idx '+str(curridx))
                extra=nums[curridx]
                extra2=max(nums[curridx+1:]) 
                extra_idx=0
                for i in range(curridx+1,len(nums)):
                    # extra=min(nums[i:])
                    if nums[i]<=extra2 and nums[i]>extra:
                        extra2=nums[i]
                        extra_idx=i

                # print(curridx,extra,extra2,extra_idx)
                extra=nums[curridx]
                nums[curridx]=extra2
                nums[extra_idx]=extra
                
                print("nums 1",nums)
                extra=101
                for i in range(curridx+1,len(nums)):
                    print("nums iter",nums)
                    myMin=min(nums[i:])
                    myMinIdx=nums[i:].index(myMin)+i
                    extra=nums[i]
                    nums[i]=myMin
                    nums[myMinIdx]=extra

                    # extra=nums[i]
                    # nums[i]=myMin




            # print(nums[:curridx+1],list(reversed(nums[curridx+1:])))
            # nums=nums[:curridx+1]+list(reversed(nums[curridx+1:]))
            print('branch 4')
            print(nums)