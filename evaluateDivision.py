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

# correct answer
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results



# over time answer

class Solution:
    
        
        
    def calcEquation(self, equations, values, queries):
        gra_dict={}
        lk_dict={}
        alp_set=set()
        vst=set()
        cnn_lst=[set()]
        
        
        for i in range(len(equations)):
            gra_dict[tuple(equations[i])]=values[i]
            gra_dict[tuple(reversed(equations[i]))]=1/values[i]
            
            lk_dict[tuple(equations[i])]=[]
            lk_dict[tuple(reversed(equations[i]))]=[]
            
            alp_set.add(equations[i][0])
            alp_set.add(equations[i][1])
            
            vst.add(tuple(equations[i]))
            vst.add(tuple(reversed(equations[i])))
        ret=[]
        for i in range(len(queries)):
            if queries[i][0]==queries[i][1]:
                if queries[i][0] in alp_set:
                    ret.append(float(1))
                else:
                    ret.append(float(-1))
                # print("branch a")
            else:
                # print("branch b")
                ret.append(self.search(queries[i][0],queries[i][1],vst,gra_dict))
        return ret
    def search(self, src,dest,vst,gra_dict):
        res=-1
        print(src,dest,vst,gra_dict)
        for i in list(vst):
            print("branch 4")
            if i[0]==src:
                print("branch 5")
                if i[1]==dest:
                    print("branch 1")
                    return gra_dict[tuple(i)]
                else:
                    print("branch 2")
                    nsrc=i[1]
                    nvst=vst.copy()
                    nvst.remove(i)
                    print(nvst,"nvst")
                    res_x=gra_dict[tuple(i)] * self.search(src=nsrc,dest=dest,vst=nvst,gra_dict=gra_dict)
                    # print(res_x)
                    if res_x>0:
                        print("branch 3")
                        res=res_x
                        break
            else:
                print("branch 6")
                pass
    
        return res


        

            





        