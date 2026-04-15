from collections import deque 

def bfs(graph,start):
    visited=set()
    queue=deque()
    
    visited.add(start)
    queue.append(start)
    
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
 
#you can edit the graph                
graph={
    0:[1,2],
    1:[3,4,5],
    2:[4,5,6],
    3:[],
    4:[],
    5:[],
    6:[7],
    7:[]
}

bfs(graph,0)
