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
   node1=Node("S");
   node2=Node("T");
   node3=Node("X");
   node4=Node("Y");
   node5=Node("Z");
   edge1 = Edge(6,node1,node2);
   edge2 = Edge(5,node2,node3);
   edge3 = Edge(-2,node3,node2);
   edge4 = Edge(8,node2,node4);
   edge5 = Edge(-4,node2,node5);
   edge6 = Edge(7,node1,node4);
   edge7 = Edge(-3,node4,node3);
   edge8 = Edge(9,node4,node5);
   edge9 = Edge(7,node5,node3);
   edge10 = Edge(2,node5,node1);
   
   node1.adjacenciesList.append(edge1);
   node1.adjacenciesList.append(edge6);
   node2.adjacenciesList.append(edge2);
   node2.adjacenciesList.append(edge4);
   node2.adjacenciesList.append(edge5);
   node3.adjacenciesList.append(edge3);
   node4.adjacenciesList.append(edge7);
   node4.adjacenciesList.append(edge8);
   node5.adjacenciesList.append(edge9);
   node5.adjacenciesList.append(edge10);

   vertexList =[node1,node2,node3,node4,node5];
   edgeList = [edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10];
   algorithm.calculateShortestPath(vertexList,edgeList,node1);
   algorithm.getShortestPathTo(node5);







