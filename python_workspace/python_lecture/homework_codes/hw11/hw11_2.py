# 파일명: hw11_2.py
# 작성자: 유태욱
# 작성일자: 2022-11-16
# 주요기능: 가중치를 가지는 그래프 객체를 통해 국내 도시 간 최단 거리 경로 탐색 프로그램
# 최종수정일자: 2022-11-19
# 수정내용: 로그 파일 닫기 함수 주석 처리

from MyGraph import *  # 그래프 클래스를 사용하기 위한 MyGraph 모듈 import


def initGraph(ICD_FILE_NAME):  # 입력받은 파일 이름의 파일 데이터로 그래프를 초기화 하는 함수
    G = WeightedGraph()  # 가중치 그래프 초기화
    f = open(ICD_FILE_NAME, 'r')  # 입력 파일 open

    while True:  # 무한 루프
        line = f.readline()  # 파일에서 1줄 입력 받는다
        if line == '':  # 빈 줄이라면
            break  # 루프문을 나간다
        src, dest, cost = line.split()  # 읽은 데이터를 각각 src,dest,cost로 나눠 준다.
        src_node, dest_node, weight = Node(src), Node(dest), int(cost)  # src와 dest를 노드로 만들고, cost를 정수로 변환해 weight에 저장
        if src not in G.node_names:  # src 노드가 그래프에 없다면
            G.add_node(src_node)  # 그래프에 노드를 추가해 준다.
        if dest not in G.node_names:  # dest 노드가 그래프에 없다면
            G.add_node(dest_node)  # 그래프에 노드를 추가해 준다.

        edge1 = WeightedEdge(src, dest, weight)  # src->dest 간선 생성
        edge2 = WeightedEdge(dest, src, weight)  # dest->src 간선 생성 (무방향성 그래프를 만들기위해)

        # 각 간선을 그래프에 추가해 준다.
        G.add_edge(edge1)
        G.add_edge(edge2)

    return G  # 그래프를 반환해 준다.


EdgesPerLine = 5  # 출력 형식을 위해 한 줄에 출력될 간선의 개수 지정

if __name__ == "__main__":  # main함수라면
    G = initGraph("KR_InterCityDist.txt")  # 입력 파일의 이름을 넣어 그래프를 초기화 한다.
    node_names = G.getNodeNames()  # 생성된 그래프의 노드 이름들을 가져온다.
    print("\nNodes : ", node_names)  # 노드 이름들을 출력한다.
    edges = G.getWEdges()  # 생성된 그래프의 간선들을 가져온다
    print("\nEdges :")  # 간선 출력 시작문
    eCount = 0  # 간선 카운팅 변수 (한 줄에 정해진 개수의 간선만 출력 하기 위해)
    for e in edges:  # 가져온 간선들을 순회하는 반복문
        print(" {}".format(e), end=', ')  # 출력 형식에 맞추어 간선을 출력한다.
        eCount += 1  # 간선 카운팅 변수를 1 증가시킨다.
        if eCount % EdgesPerLine == 0:  # 한 줄에 출력될 간선의 개수만큼 나누어 떨어진다면
            print()  # 개행 출력
    G.printConnectivity()  # 각각의 노드가 연결된 인접 노드를 출력
    G.print_inter_city_table()  # 노드 간 거리를 나타내는 테이블을 출력

    path_Dijkstra, path_cost = Dijkstra(G, "GJ", "SC")  # GJ->SC 최소거리 계산
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("GJ", "SC", path_Dijkstra, path_cost))  # 계산 결과 출력
    path_Dijkstra, path_cost = Dijkstra(G, "SC", "GJ")  # SC->GJ 최소거리 계산
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("SC", "GJ", path_Dijkstra, path_cost))  # 계산 결과 출력
    path_Dijkstra, path_cost = Dijkstra(G, "SL", "BS")  # SL->BS 최소거리 계산
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("SL", "BS", path_Dijkstra, path_cost))  # 계산 결과 출력
    path_Dijkstra, path_cost = Dijkstra(G, "BS", "SL")  # BS->SL 최소거리 계산
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("BS", "SL", path_Dijkstra, path_cost))  # 계산 결과 출력
    # close_file()  # 로그 저장을 위해 사용한 파일 닫기

