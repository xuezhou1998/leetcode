# The key issue in this problem is how arrange the
# intervals in the most compact way.
# To acheive this goal, we need to tietly arange one
# interval right after another interval.
# First we will sort the invervals by their start time, and then
# we create the first room with the first interval,
# which is the one starts the earliest.
# And then for each room we only need to record the latest
# inverval end time. Before each time we iterate a interval,
# We sort the existing rooms by their cooresponding end time.
# And when a new interval comes, we compare
# the new interval's start time and the end time in each existing room,
# if the start time is larger than the existing room's end time,
# then add this interval to that room, and update that room's end time
# to the end time of the current interval, and break from the
# loop of existing rooms.
#
# in the case when on existing room's end time is smaller than
# the current interval's start time, we create a new room and record
# its end time with the end time of the current interval.



class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals)
        # print(intervals)
        ctlst=[]
        ctlst.append(max(intervals[0]))
        ctr=0
        for i in range(len(intervals)):
            # print(i)
            if ctr==0:
                ctr+=1
                continue
            else:
                put=False
                ctr+=1
                ctlst=sorted(ctlst)
                for j in range(len(ctlst)):
                    # print(i,j,'x')
                    if ctlst[j]<=min(intervals[i]):
                        ctlst[j]=max(intervals[i])
                        put=True
                        # print(j)
                        break
                if put==False:
                    # print(i,j)
                    ctlst.append(max(intervals[i]))
        return len(ctlst)





# below is a wrong example:



# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         # print (self.isOverlap([2,4],[,5]))
#         contlst=[]
#         contlst.append([intervals[0]])
#
#         for i in range(1,len(intervals)):
#             put=False
#             for j in range(len(contlst)):
#                 if self.isOverlapCont(contlst[j],intervals[i])==False:
#                     contlst[j].append(intervals[i])
#                     put=True
#             if put==False:
#                 contlst.append([intervals[i]])
#         return len(contlst)
#
#     def isOverlapCont(self, cont:List[List[int]], intv:List[int])->bool:
#         ret=False
#         for i in range(len(cont)):
#             ret=self.isOverlap(cont[i],intv)
#             if ret==True:
#                 break
#         return ret
#
#     def isOverlap(self, intv1:List[int],intv2:List[int])->bool:
#         if min(intv1)<min(intv2) and max(intv1)>min(intv2):
#             return True
#         elif min(intv1)>min(intv2) and min(intv1)<max(intv2):
#             return True
#         elif min(intv1)==min(intv2) or max(intv1)==max(intv2):
#             return True
#         else:
#             return False
