from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        hash_table=defaultdict(dict)
        for equation,value in zip(equations,values):
            hash_table[equation[0]][equation[1]]=value
            hash_table[equation[1]][equation[0]]=1/value
        
        vis={}
        for key in hash_table:
            vis[key]=False
        def check(pre,fenzi,fenmu):
            if fenzi not in hash_table or vis[fenzi]:
                return None
            vis[fenzi]=True
            if fenmu in hash_table[fenzi]:
                vis[fenzi]=False
                return pre*hash_table[fenzi][fenmu]
            else:
                for fenmu1 in hash_table[fenzi]:
                    res=check(pre*hash_table[fenzi][fenmu1],fenmu1,fenmu)
                    if res:
                        vis[fenzi]=False
                        return res
                vis[fenzi]=False
                return None
        ans=[]
        for query in queries:
            if query[0]==query[1] and query[0] in hash_table:
                ans.append(1.0)
            else:
                t=check(1,query[0],query[1])
                if t:
                    ans.append(t)
                else:
                    ans.append(-1.0)
        return ans


equations=[["a","b"],["b","c"]]
values=[2.0,3.0]
queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations,values,queries))
print(Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))