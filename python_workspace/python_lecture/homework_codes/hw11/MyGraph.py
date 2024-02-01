# 파일명: MyGraph.py
# 작성자: 유태욱
# 작성일자: 2022-11-16
# 주요기능: 가중치를 가지는 그래프 클래스를 구현한 모듈
# 최종수정일자: 2022-11-19
# 수정내용: 로그문 주석 처리

import sys  # 정수 maxsize 호출과 로그의 함수 이름 표시를 위한 sys 모듈 import


# f = open("log_태욱.txt", 'w')  # 로그 표시 파일 open


class Node(object):  # 그래프를 구성하는 Node 클래스
    def __init__(self, name):  # 객체 생성자 함수
        self.name = name  # 이름을 초기화

    def getName(self):  # 이름 getter 함수
        # f.write("LOG/Node.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        return self.name  # 이름을 반환한다.

    def __str__(self):  # 객체의 문자열을 반환 해 주는 함수
        # f.write("LOG/Node.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        return str(self.name)  # 객체의 이름을 반환해 준다.


class Edge(object):  # 그래프를 구성하는 Edge 클래스
    def __init__(self, src, dest):  # 객체 생성자 함수
        self.src = src  # 출발지 초기화
        self.dest = dest  # 목적지 초기화

    def getSource(self):  # 출발지 getter 함수
        # f.write("LOG/Edge.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        return self.src  # 출발지를 반환해 준다.

    def getDestination(self):  # 도착지 getter 함수
        # f.write("LOG/Edge.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        return self.dest  # 도착지를 반환해 준다.

    def __str__(self):  # 객체의 문자열을 반환해 주는 함수
        # f.write("LOG/Edge.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        return "{:3}->{:3}".format(self.src, self.dest)  # 출발지->도착지 형식의 문자열을 반환해 준다.


class WeightedEdge(Edge):  # 그래프를 구성하며 가중치가 있는 WEdge 클래스
    def __init__(self, src, dest, weight):  # 객체 생성자 함수
        Edge.__init__(self, src, dest)  # Edge를 상속받아 Edge의 생성자를 사용해 src와 dest를 초기화
        self.weight = weight  # 가중치(비용) 초기화한다.

    def getWeight(self):  # 가중치 getter 함수
        # f.write("LOG/WEdge.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        return self.weight  # 가중치를 반환해 준다.

    def __str__(self):  # 객체의 문자열을 반환해 주는 함수
        # f.write("LOG/WEdge.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        return "{}--{}->{}".format(self.src, self.weight, self.dest)  # 출발지-비용->도착지 형식의 문자열을 반환해 준다.


class WeightedGraph(object):  # 가중치를 가진 그래프 클래스
    def __init__(self):  # 객체 생성자 함수
        self.nodes = []  # 노드가 저장될 리스트
        self.node_names = []  # 노드의 이름들이 저장될 리스트
        self.wedges = []  # wedge들이 저장될 리스트
        self.adjacency_list = {}  # 노드:리스트 꼴로 저장될 인접 노드 dictionary
        self.edge_weights = {}  # (src,dest):weight 꼴로 저장될 간선 가중치 dictionary

    def add_node(self, node):  # 그래프에 노드를 추가하는 함수
        if node in self.nodes:  # 입력받은 노드가 이미 객체의 노드리스트에 있다면
            raise ValueError("노드 중복")  # 중복 에러 raise
        else:  # 그 외의 경우
            self.nodes.append(node)  # 노드 리스트에 추가한다
            self.node_names.append(node.getName())  # 노드 이름 리스트에 이름을 추가한다
            self.adjacency_list[node.getName()] = []  # 인접 노드 dictionary를 초기화한다.

    def add_edge(self, edge):  # 그래프에 간선을 추가하는 함수
        src = edge.getSource()  # 간선의 출발 노드를 가져온다
        dest = edge.getDestination()  # 간선의 도착 노드를 가져온다
        if not (src in self.node_names and dest in self.node_names):  # 출발노드 도착노드 둘 중 하나라도 그래프에 없는 경우
            raise ValueError("노드가 없음")  # 노드 없음 에러 raise
        self.wedges.append(edge)  # 가중치를 가진 간선 리스트에 간선을 추가한다.
        self.adjacency_list[src].append(dest)  # 인접 노드 리스트에 출발노드 위치의 리스트에 도착노드를 추가한다
        self.edge_weights[(src, dest)] = edge.getWeight()  # 간선의 가중치를 저장한다.

    def getNeighbors(self, node):  # 입력 받은 노드에 인접한 노드 리스트를 반환하는 함수
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        # f.write("LOG/WGraph.{}(): parameter {} is {}type \n".format(sys._getframe().f_code.co_name, node,type(node)))  # 로그문
        # f.write("LOG/WGraph.{}}(): output {} is {} type \n".format(sys._getframe().f_code.co_name,self.adjacency_list[node],type(self.adjacency_list[node])))  # 로그문
        return self.adjacency_list[node]  # 노드의 인접 노드 리스트 반환

    def getAdjacencyList(self):  # 인접 노드 dictionary getter 함수
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        # f.write("LOG/WGraph.{}(): output {} type \n".format(sys._getframe().f_code.co_name,type(self.adjacency_list)))  # 로그문
        return self.adjacency_list  # 인접 노드 dictionary 반환

    def getNodeNames(self):  # 노드 이름 리스트 getter 함수
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        # f.write("LOG/WGraph.{}(): output {} type \n".format(sys._getframe().f_code.co_name, type(self.node_names)))  # 로그문
        return self.node_names  # 노드 이름 리스트 반환

    def getNodes(self):  # 노드 리스트 getter 함수
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        # f.write("LOG/WGraph.{}(): output {} type \n".format(sys._getframe().f_code.co_name, type(self.nodes)))  # 로그문
        return self.nodes  # 노드 리스트 반환

    def getWEdges(self):  # 가중치 간선 리스트 getter
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        # f.write("LOG/WGraph.{}(): output {} type \n".format(sys._getframe().f_code.co_name, type(self.wedges)))  # 로그문
        return self.wedges  # 가중치 간선 리스트 반환

    def getEdgeWeight(self, edge):  # 입력 받은 간선의 가중치를 반환하는 함수
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        # f.write("LOG/WGraph.{}(): parameter {} is {} type\n".format(sys._getframe().f_code.co_name, edge,type(edge)))  # 로그문
        if (edge.src, edge.dest) in self.edge_weights:  # 가중치 dictionary에 간선이 있다면
            # f.write("LOG/WGraph.{}(): output {} type \n".format(sys._getframe().f_code.co_name,type(self.node_names)))  # 로그문
            return self.edge_weights[(edge.src, edge.dest)]  # 가중치 반환
        else:
            # f.write("LOG/WGraph.{}(): Edge none\n".format(sys._getframe().f_code.co_name))  # 로그문
            None

    def printConnectivity(self):  # 각 노드에 연결된 인접 노드를 출력하는 함수
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        print("\n\nAdjacent Nodes Print:")
        for node in self.node_names:  # 노드 이름을 순회하는 반복문
            print(" AdjacencyList[{}] = {}".format(node, self.adjacency_list[node]))  # 각 노드의 인접 노드를 출력한다

    def print_inter_city_table(self):  # 노드 간 거리를 나타내는 테이블을 출력하는 함수
        print("\nInitial Inter City Weight Table:")
        l = len(self.node_names)  # 그래프 내 노드의 개수 변수 선언
        print("     |", end='')  # 구분선 출력
        for i in range(l):  # 그래프 내의 노드 개수 만큼 반복 하는 반복문
            print("{:>5}".format(self.node_names[i]), end='')  # 노드 리스트의 i번째 노드 이름을 출력 형식에 맞춰 출력 한다.
            if i == l - 1:  # 마지막 출력이면
                print()  # 개행 삽입
        print("-----" + "+" + "-----" * l, end='')  # 구분선 출력
        for row in range(l):  # 그래프 내의 노드 개수 만큼 행 반복
            print("\n{:^5}".format(self.node_names[row]), end='|')  # 노드 리스트의 row 번째 노드 이름을 출력 형식에 맞춰 출력 한다.
            src = self.node_names[row]  # 출발 노드의 이름 변수 선언
            for col in range(l):  # 그래프 내의 노드 개수 만큼 열 반복
                dest = self.node_names[col]  # 도착 노드의 이름 변수 선언
                if src == dest:  # 두 노드가 같은 경우
                    print("{:>5}".format("0"), end='')  # 0 출력
                elif (src, dest) not in self.edge_weights.keys():  # 인접해 있지 않은 경우
                    print("{:>5}".format("INF"), end='')  # 무한대 출력
                else:  # 그 외의 경우
                    print("{:>5}".format(self.edge_weights[(src, dest)]), end='')  # 노드간 가중치 출력
        print("\n")  # 개행 두 개 출력(마지막에 end='' 해 주었기 때문)

    def __str__(self):  # 객체의 문자열을 반환해 주는 함수
        # f.write("LOG/WGraph.{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
        string = ""  # 빈 문자열 초기화
        for s in self.nodes:  # 노드 리스트를 순회하며 출발지가 되는 노드를 s로 반복
            for d in self.wedges[s]:  # 간선 리스트를 순회하며 출발지가 s인 노드들을 순회하며 도착지가 되는 노드를 d로 반복
                string += "{:3}->{:3}".format(s.getName(), d.getName())  # 출력 형식에 맞춰 빈 문자열에 추가
        return string  # 문자열 반환


def printPath(path):  # 경로를 출력하는 함수
    # f.write("LOG/{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
    string = ""  # 빈 문자열 초기화
    for i in range(len(path)):  # 경로 리스트의 길이만큼 반복하는 반복문
        string += str(path[i])  # 문자열에 현재 도시의 이름을 덧붙인다
        if i != len(path) - 1:  # 마지막 도시 출력이 아니라면
            string += '->'  # 도시를 이어주는 화살표도 함께 덧붙임
    return string  # 결과 문자열을 반환


PLUS_INF = sys.maxsize  # 다익스트라 알고리즘에서 무한대 가중치로 사용할 정수 최대값 선언


def Dijkstra(G, start, end):  # 다익스트라 알고리즘을 통해 start 노드부터 end 노드까지 최소 거리와 경로를 반환해 주는 함수.
    # f.write("LOG/{}(): called\n".format(sys._getframe().f_code.co_name))  # 로그문
    errorInLoop = False  # 루프문 내에서 오류 검출 flag 변수 선언
    nodeAccWeight = {}  # 출발 노드에서 각 노드까지의 거리를 저장하는 dictionary 변수 선언
    nodeStatus = {}  # 노드의 상태를 저장하는 dictionary 변수 선언
    prevNodes = {}  # 노드의 이전 노드를 저장하는 dictionary 변수 선언
    selectedNodes = []  # 선택된 노드를 저장하는 리스트 선언(최소 거리가 될 수 있는 노드를 모으는 리스트)
    remainingNodes = []  # 남아있는 노드를 저장하는 리스트 선언
    # Edges = G.getWEdges()
    for node in G.node_names:  # 그래프의 노드를 순회하는 반복문 - 출발노드에서 각 노드까지의 거리를 초기화하는 반복문
        e = Edge(start, node)  # 출발 노드부터 순회하는 노드(node)까지의 경로 만들기
        # f.write("LOG/{}(): first for loop = e({})\n".format(sys._getframe().f_code.co_name, e)) # 로그문
        # f.write("LOG/{}(): first for loop = start({})\n".format(sys._getframe().f_code.co_name, start)) # 로그문
        # f.write("LOG/{}(): first for loop = end({})\n".format(sys._getframe().f_code.co_name, end)) # 로그문
        if node == start:  # 만약 node가 출발 노드와 같다면
            weight = 0  # 가중치는 0
        else:  # 그외의 경우에는
            weight = G.getEdgeWeight(e)  # 생성한 경로의 가중치를 getter로 가져온다
            if weight == None:  # 만약 생성한 경로가 그래프에 없다면(두 노드가 인접되어있지 않다면)
                weight = PLUS_INF  # 두 노드간 거리를 무한대로 설정한다.
        # f.write("LOG/{}(): first for loop = weight({})\n".format(sys._getframe().f_code.co_name, weight)) # 로그문
        # print(" Initial weight of edge ({}) = {}: ".format(e, weight))
        nodeAccWeight[node] = weight  # node 까지의 가중치를 저장한다.
        nodeStatus[node] = False  # node의 방문 상태를 False로 저장한다.
        prevNodes[node] = start  # node의 이전 노드를 출발 노드로 저장한다.
        if node != start:  # 만약 node가 출발 노드와 다른 노드라면
            remainingNodes.append(node)  # 남은 노드(탐색 해야 할 노드 리스트)에 추가한다.

    # f.write("LOG/{}(): first for loop result = remainingNodes({})\n".format(sys._getframe().f_code.co_name, remainingNodes)) # 로그문
    nodeAccWeight[start] = 0   # 출발 노드에서 출발 노드까지의 거리는 0으로 저장한다.
    nodeStatus[start] = True  # 출발 노드는 방문한 처리한다.
    selectedNodes.append(start)  # 선택된 노드 처음에 출발 노드를 추가해준다.

    # count = 1
    while len(remainingNodes) != 0:  # 탐색 해야 할 노드 리스트가 비어 있을 때까지 반복 하는 반복문
        minAccWeight = PLUS_INF  # 최소 인접 가중치를 무한대 값으로 초기화 한다.
        minNode = None  # 최소 거리의 노드를 None으로 초기화한다.
        
        for n in remainingNodes:  # 탐색할 노드 리스트를 순회 하는 반복문 (현재 노드 위치에서 최소 거리로 이동할 노드를 찾는 반복문)
            nAccWeight = nodeAccWeight[n]  # 출발 노드에서 순회 노드 n 까지의 거리를 가져온다
            if nAccWeight != None and nAccWeight < minAccWeight:  # 인접한 노드이며, 무한대 보다 작은 가중치를 갖는 경우
                minNode, minAccWeight = n, nodeAccWeight[n]  # 최소 거리 노드와 최소 가중치를 변경해 준다.
        if minNode == None:  # 만약 최소노드를 찾지 못했다면
            # 오류문 출력
            print("No minNode was selected at this round !!")
            print("Error - graph is not fully connected !!")
            errorInLoop = True  # 에러 있음을 표시
            break  # 반복문을 종료한다.
        else:  # 최소 노드를 찾은 경우에는
            selectedNodes.append(minNode)  # 선택된 노드에 최소 비용 노드를 추가해 준다.
            minAccWeight = nodeAccWeight[minNode]  # 최소 가중치를 갱신해 준다.
            for rn in remainingNodes:  # 남아 있는 노드를 다시 순회 하며
                if rn == minNode:  # 남아 있는 노드가 최소 노드와 같다면
                    continue  # 반복문 진행
                e = Edge(minNode, rn)  # 최소 노드와 순회 중인 남은 노드(rn)과의 간선을 만든다
                eWeight = G.getEdgeWeight(e)  # 생성한 간선의 가중치를 그래프에서 가져온다
                if eWeight is None:  # 두 노드가 서로 인접하지 않는 경우에는
                    continue  # 반복문을 진행한다.
                if nodeAccWeight[rn] > minAccWeight + eWeight:  # 가져온 가중치와 최소 가중치의 합이 시작 노드에서부터 rn 노드까지의 가중치보다 작다면
                    nodeAccWeight[rn] = minAccWeight + eWeight  # 시작 노드에서 rn 노드까지의 가중치를 해당 값으로 수정하고
                    prevNodes[rn] = minNode  # rn의 이전 노드를 최소 노드로 설정한다.
            if minNode == end:  # 만약 최소 노드가 도착 노드라면
                break  # while 반복문을 종료한다.
            remainingNodes.remove(minNode)   # 최소 노드를 남아있는 노드에서 지운다.
        # count += 1
    if errorInLoop:  # 루프문을 종료 후 오류가 있었다면
        return None  # None 반환
    print(" prevNode : ", prevNodes)  # 이전 노드로 연결된 노드들을 출력한다.
    path = [end]  # 최소 경로 리스트 변수를 초기화 하고 도착 노드를 넣어준다.
    cur_node = end  # 현재 노드를 도착 노드로 설정한다.
    while cur_node in selectedNodes:  # 현재 노드가 선택된 노드 내에 있을때만 반복하는 반복문 (prevNodes를 역주행하며 경로를 만들어 내는 반복문)
        if cur_node == start:  # 현재 노드가 출발 노드라면
            break  # 반복문을 종료한다.
        else:  # 그 외의 경우에는
            cur_node = prevNodes[cur_node]  # 현재 노드의 이전 노드를 현재 노드로 설정해준다.
            path.insert(0, cur_node)  # 현재 노드를 경로에 추가해준다.

    return path, nodeAccWeight[end]  # 최단 거리 경로와 소요 가중치를 반환한다.

#
# def close_file():
#     global f
#     f.write("LOG/{}(): called = close this log file\n".format(sys._getframe().f_code.co_name))
#     f.close()
#     return
