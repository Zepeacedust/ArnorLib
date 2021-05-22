from PIL import Image


from typing import List
from Datastructures import PrioQueue


class Connection:
    def __init__(self, end, weight):
        self.End = end
        self.Weight = weight

class Node:
    def __init__(self, connections, name):
        self.Connections = connections
        self.Name = name
    def __str__(self) -> str:
        return self.Name

class PathfindingNode(Node):
    def __init__(self, connections, name):
        Node.__init__(self, connections, name)
        self.Distance = -1
        self.Root = None
    
    
class Graph:
    def __init__(self, Nodes):
        self.Nodes = Nodes
        
    def __getitem__(self, index):
        return self.Nodes[index]
    
    def FindRoute(self, start:PathfindingNode, end:PathfindingNode):
        for node in self.Nodes:
            node.Distance = -1
            node.Root = None
        start.Distance = 0
        availableTiles = PrioQueue(key=lambda x: x.Distance)
        availableTiles.add(start)
        while end.Distance == -1 and not availableTiles.isEmpty:
            operatingNode = availableTiles.pop()
            for connection in operatingNode.Connections:
                newNode = connection.End
                if newNode.Distance == -1 or operatingNode.Distance + connection.Weight < newNode.Distance:
                    newNode.Distance = operatingNode.Distance + connection.Weight
                    newNode.Root = operatingNode
                    availableTiles.add(newNode)
        path = [end]
        while path[-1].Root != None:
            path.append(path[-1].Root)
        return path[::-1]
                            
world = Graph([
    PathfindingNode([],"0"),
    PathfindingNode([],"1"),
    PathfindingNode([],"2"),
    PathfindingNode([],"3")
])

world[0].Connections.append(Connection(world[1],7))
world[0].Connections.append(Connection(world[3],1))
world[1].Connections.append(Connection(world[2],1))
world[3].Connections.append(Connection(world[2],1))

print(*world.Nodes)
shortestPath = world.FindRoute(world[0],world[2])
print(*shortestPath)

print(shortestPath[-1].Distance)