''' given a list of packages that need to be built and the dependencies for each package
 determine a valid order in which to build

0: [4]
1: [0]
2: [0]
3: [1,2]
4: [3]

'''
def build_pgk(g):
    ret=[]
    explored=set([])
    active=set([])
    def dfs(v):
        active.add(v)
        for u in g[v]:
            if u in active:
                raise Exception("dependency graph has cycle")
            if u not in explored:
                explored.add(u)
                dfs(u)
        active.remove(v)
        explored.add(v)
        ret.append(v)

    for v in g.keys():
        if v not in explored:
            dfs(v)

    return ret

g = {0:[4],1:[0],2:[0],3:[1,2],4:[3]}
print(build_pgk(g))
