class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # seems like union find
        # we find what component makes it connected components > 1

        # for every edge, we connect it
        # once we get to one connected component, and there's still elements in the list
        # not sure from here. 

        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1

        components = len(par)
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            