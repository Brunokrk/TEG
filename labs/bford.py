    #import sys:

class Node(object):

    def __init__ (self,name):
        self.name = name;
        self.visited = False;
        self.adjacenciesList = [];
        self.predecessor = None;
        self.minDistance = 999999;


class Edge(object):

    def __init__ (self,weight,startVertex,targetVertex):
        self.weight = weight;
        self.startVertex = startVertex;
        self.targetVertex = targetVertex;

class Algorithm(object):

    HAS_CYCLE = False;

    def calculateShortestPath(self, vertexList, edgeList, startVertex):

        startVertex.minDistance =0;
        for i in range (0,len(vertexList)-1):
            for edge in edgeList:
                u = edge.startVertex;
                v = edge.targetVertex;
                newDistance = u.minDistance + edge.weight;

                if newDistance < v.minDistance:
                    v.minDistance = newDistance;
                    v.predecessor = u;
        
        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected");
                Algorithm.HAS_CYCLE = True;
                return;

    def hasCycle(self,edge):
        if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
            return True;
        else:
            return False;

    def getShortestPathTo(self,targetVertex):
        
        if not Algorithm.HAS_CYCLE:
            print ("Caminho minimo e: ", targetVertex.minDistance);

        node = targetVertex;
        while node is not None:
            print("%s : ", node.name);
            node = node.predecessor;


if __name__ == '__main__':
	
   algorithm = Algorithm();
   node1=Node("A");
   node2=Node("B");
   node3=Node("C");
   node4=Node("D");
   edge1 = Edge(1,node1,node2);
   edge2 = Edge(20,node2,node3);
   edge3 = Edge(1,node3,node4);
   edge4 = Edge(-10,node3,node2);
   edge5 = Edge(300,node1,node4);
   node1.adjacenciesList.append(edge1);
   node1.adjacenciesList.append(edge2);
   node2.adjacenciesList.append(edge3);
   node3.adjacenciesList.append(edge4);
   node3.adjacenciesList.append(edge2);

   vertexList =[node1,node2,node3,node4];
   edgeList = [edge1,edge2,edge3,edge4,edge5];
   algorithm.calculateShortestPath(vertexList,edgeList,node1);
   algorithm.getShortestPathTo(node4);







