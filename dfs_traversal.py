#By recursion
def dfs(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)
            
#Graph (Can be Changed)

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [5],
    5: []
}
visited=set()
dfs(graph,0,visited)


''' #Manually

def dfs(graph,start):
    visited=set()
    stack=[start]
    
    while stack:
    node=stack.pop()
    
    if node not in visited:
        print(node, end="  ")
        visited.add(node)
        
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
                
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [5],
    5: []
}

dfs(graph, 0)                
'''


    
    
    
    
