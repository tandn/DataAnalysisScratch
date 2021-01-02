# ajdency list
# 1 -> []
# 2 -> [1]
# 3 -> [2]
# 4 -> [2]
# 5 -> [4]
# 6 -> [3]
# 7 -> [5,6]
#g={'a':['b','d'],'b':['e'],'c':['e','f'],'d':['b'],'e':['d'],'f':['f']}
g={'a':['b'],'b':['c'],'c':['d'],'d':[],'e':['a']}
paths=[]
s=1
def path(t,p,cur_len):
    if len(p) > cur_len:
        p[cur_len] = t
    else:
        p.append(t)

    cur_len+=1
    if s==t:
        paths.append(p[::-1])
    else:
        for u in g[t]:
            path(u,p,cur_len)

def dfs():
    parent={}
    active={}
    def dfs_visit(s):
        for u in g[s]:
            if u not in parent:
                parent[u]=s
                dfs_visit(u)
            elif active[s]:
                print("has cycle")

    for s in g.keys():
        print(parent)
        if s not in parent:
            active[s]=True
            parent[s] = None
            dfs_visit(s)
            active[s]=False




#print(paths)
#path(7,[],0)

#paths=list(map(lambda p: p.reverse() or p, paths))
dfs()
#print(parent)
