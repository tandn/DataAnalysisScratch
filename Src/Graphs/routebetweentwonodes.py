def route(g,s,t):
    visited=set([])
    visited.add(s)

    def dfs(u):
        stack=[]
        stack.append(u)
        while stack:
            v=stack.pop()
            for w in g[v]:
                if w == t:
                    return True
                if w not in visited:
                    visited.add(v)
                    stack.append(w)
        return False

    def bfs(u):
        queue=[]
        queue.insert(0,u)
        while queue:
            v=queue.pop()
            for w in g[v]:
                if w == t:
                    return True
                if w not in visited:
                    queue.insert(0,w)
                    visited.add(w)
        return False
    return bfs(s)

g={'a':['b'],'b':['c'],'c':['d'],'d':[],'e':['a']}
print(route(g,'d','e'))
print(route(g,'e','d'))
