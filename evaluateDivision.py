'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

'''




# class Solution:
#     def calcEquation(self, equations, values, queries):
#         ret=[]
#         eql_dict={}
#         conn_set=set()
#         for i in range(len(equations)):
#             eql_dict[equations[i]]=values[i]
#         for i in range(len(equations)):
#             conn_set.add(tuple(sorted(i)))
#             sub_eq=equations.copy().remove(equations[i])
#             for j in range(len(sub_eq)):
#                 conn_set.add(tuple(sorted(j)))
#                 my_union=set(equations[i]).union(set(sub_eq[j])) 
#                 if my_union !=None:
#                     conn_set.add(tuple(sorted(list())))

#         for i in range(len(queries)):
#             if queries[i] in equations:
#                 ret.append(eql_dict[queries[i]])
#             else:



class Solution:
    def calcEquation(self, equations:list, values, queries):
        cnn_set=set()
        lk_dict={}
        for i in equations:
            lk_dict[i]=[]
        left_lst=equations
        while len(left_lst)>0:
            ele=left_lst.pop()
            for i in range(len(left_lst)):
                if left_lst[i][0]==ele[0]:
                    lk_dict[ele]=left_lst[i]
                else:
                    pass
            





        