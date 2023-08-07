### 그래프의 정의

- 그래프(Graph) **G=(V, E)** : 연결되어 있는 객체 간의 관계를 표현하는 자료구조로, 가장 일반적인 자료구조 형태 중 하나라고 할 수 있다.
  - ex)트리(tree), 전기 회로의 소자 간 연결 상태, 운영체제의 프로세스-자원 관계, 지도에서 도시들의 연결 상태 등

- 정점(vertex, point, node)
  - 여러가지 특성을 가질 수 있는 객체 이며 점, 노드 등으로도 불린다.
  - V(G): 그래프 G의 정점들의 집합
  
- 간선(edge, arrow, arc, link)
  - 간선은 정점들 간의 관계를 의미한다.
  - 링크, 엣지, 아크 등으로도 불린다.
  - E(G): 그래프 G의 간선 들의 집합

<br>

### 그래프의 역사
- 1736년 오일러에 의하여 창안(konigsberg 다리문제)

|![](https://velog.velcdn.com/images/phwon7/post/6bb9af1c-aa27-43c4-bab0-dbca1365145e/image.png)|![](https://velog.velcdn.com/images/phwon7/post/716e557a-88d7-4420-ac9b-be91a28ca72f/image.png)|
|--|--|

  - A, B, C, D 지역의 연결 관계 표현
    - 위치: 정점
    - 다리: 간선
  - 오일러 문제: 모든 다리를 한 번만 건너서 처음 출발했던 장소로 돌아오는 문제
  - 오일러 정리: 모든 정점에 연결된 간선의 수가 짝수이면 오일러 경로가 존재한다.
  
<br>

### 그래프의 종류

- 무방향 그래프(Undirected Graph)
  - 무방향 간선(undirected edge)만 사용
  - 간선을 통해서 양방향으로 갈 수 있음
  - (A, B)와 같이 정점의 쌍으로 표현
  - (A, B) = (B, A)
  
  |![](https://velog.velcdn.com/images/phwon7/post/d0b64917-ac8a-4eac-a7c9-ddb211791eb8/image.png)|![](https://velog.velcdn.com/images/phwon7/post/f98d6c4e-773f-4538-83e0-28c1dac8b5c7/image.png)|
|--|--|
|V(G1)= {0, 1, 2, 3} <br> E(G1)= {(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)}|V(G2)= {0, 1, 2, 3} <br> E(G2)= {(0, 1), (0, 2))}|

<p>

- 방향 그래프(Directed Graph)
  - 방향 간선(directed edge)만 사용
  - 간선을 통해서 한 쪽 방향으로만 갈 수 있음
  - <A, B>와 같이 정점의 쌍으로 표현
  - <A, B> ≠ <B, A> 
  
  |<center>![](https://velog.velcdn.com/images/phwon7/post/45d58fae-4322-42ec-aaba-08ca0ba26daf/image.png)</center>|
  |--|
  |V(G3)= {0, 1, 2} <br> E(G3)= {<0, 1>, <1, 0>, <1, 2>}|

- 가중치 그래프(Weighted Graph)
  - 네트워크(network)라고도 함
  - 간선에 비용(cost)나 가중치(weight)가 할당된 그래프
  - ex) 정점-> 각 도시, 간선-> 도시를 연결하는 도로, 가중치-> 도로의 길이
  ![](https://velog.velcdn.com/images/phwon7/post/8a1988c0-832a-49b0-82bf-9289792deb13/image.png)

<br>

### 그래프 용어
- 부분 그래프(Subgraph)
  - 정점집합 V(G)와 간선집합 E(G)의 부분집합으로 이루어진 그래프
  - S는 G의 부분 그래프
- 인접 정점(Adjacent vertex)
  - 단 한 개의 간선으로 연결된 두 정점
  - S에서 1과 6은 인접 정점
- 차수(Degree)
  - 정점에 연결된 다른 정점의 수
  - S에서 정점 1의 차수는 2, 6의 차수는 4
  - 무방향 그래프에서 모든 차수의 합은 간선 수의 2배
  - 방향그래프의 경우 진입차수(in-degree)와
  - 진출차수(out-degree)가 있음
  - 방향그래프의 경우 모든 진입(진출)차수의 합은 간선의 수
- 경로(Path)
  - 간선이 존재하는 정점들의 나열
  - S에서 1-6-3-6-2-1 등
  - 단순 경로(Simple path)
  - 경로 중 반복되는 간선이 없는 경로
  - S에서 1-6-2-5-4-6-3 등
- 사이클(Cycle)
  - 단순 경로의 시작 정점과 종료 정점이 동일한경로
  - S에서 2-6-4-5-2 등
- 완전 그래프(Complete graph)
  - 모든 정점이 자신을 제외한 모든 정점과 인접한그래프
  - 정점 n개를 갖는 완전 그래프에서 간선의 개수는 (nx(n-1))/2 개
- 연결 그래프(Connected graph)
  - 모든 정점사이의 경로가 존재하는 그래프
  - V는 연결그래프이고 S는 비연결그래프이다.
- 트리(Tree)
  - 사이클이 존재하지 않는 연결 그래프

|그래프 G|![](https://velog.velcdn.com/images/phwon7/post/382c3aac-c869-4f44-9532-049a9cb183f1/image.png)|
|--|--|
  |<center>**그래프 G의 부분그래프**</center>|![](https://velog.velcdn.com/images/phwon7/post/2672c552-96a1-4246-b26a-87454ef0666d/image.png)|
  |<center>**완전 그래프**</center>|![](https://velog.velcdn.com/images/phwon7/post/3824f7a2-5caa-47dc-a0ad-77bc2a513c97/image.png)|
  
<br>
  

### 그래프의 ADT

![](https://velog.velcdn.com/images/phwon7/post/d0249806-f29f-433a-84a4-35a83bccc593/image.png)

<br>
  
  

### 그래프의 표현 방법
- 인접 행렬(adjecent matrix) 방법
  - 2차원 배열을 이용한 그래프 표현 방법
  - If(간선 (i, j)가 그래프에 존재) M[i][ j] = 1
    Else M[i][ j] = 0
  ![](https://velog.velcdn.com/images/phwon7/post/28b9788c-f683-4269-9df0-cbce9e0d788c/image.png)

  
- 인접 리스트(adjacent list) 방법
  - 포인터를 포함하는 구조체를 이용하여 그래프 표현
  - 각 정점에 인접한 정점들을 연결리스트로 표현
  ![](https://velog.velcdn.com/images/phwon7/post/360e9fe3-441c-443f-b3a5-816212a7d655/image.png)

<br>  
  

### 그래프 탐색
- 그래프 순회(graph traversal), 그래프 탐색(graph search) 용어가 혼용
- 그래프의 가장 기본적인 연산
- 하나의 정점으로부터 시작하여 그래프의 모든 정점들을 한 번씩 방문하는 연산
  - 예: 도로망에서 특정도시에서 다른 도시로 갈 수 있는지 여부
  - 예: 전자회로에서 특정단자와 다른 단자가 서로 연결되어 있는지 여부
- 탐색방법
  - 깊이우선 탐색(DFS : depth-first search)
  - 너비우선 탐색(BFS : breadth-first search) 
  
### 깊이 우선 탐색(DFS)
- 깊이 우선 탐색 (DFS: depth-first search)
  - 알고리즘
    - 시작 정점에서 특정한 방향으로 갈 수 있을 때까지 가다가 더 이상 갈 수 없게 되면,
    - 가장 가까운 갈림길 간선이 있던 정점으로 돌아와서 이 곳으로부터 다른 방향으로 다시 탐색을 계속하는 방법
  - 가장 마지막에 만났던 갈림길 간선의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 스택 사용
  - 순환함수 호출로 묵시적인 스택 이용 가능


- DFS 알고리즘(재귀 버전)

  |![](https://velog.velcdn.com/images/phwon7/post/e65f315c-76fa-4b5a-b60a-c2fad1a9dec0/image.png)|
  |--|
  |![](https://velog.velcdn.com/images/phwon7/post/479f0430-0568-40d7-b08e-43976807d71f/image.png)|

- DFS의 성능 분석
  - 깊이 우선 탐색 기법은 그래프의 모든 간선을 조사
  - 인접 리스트로 표현 된 경우, 
    - O(n+e), n은 노드의 수, e는 간선의 수
  - 인접 행렬로 표현된 경우
    ![](https://velog.velcdn.com/images/phwon7/post/24be8ed9-7e5a-477c-9b21-06fcb2020b33/image.png)
    - O(n2)
  - 희소 행렬인 경우에는 인접 리스트가 훨씬 효과적임을 의미
    - C.f> 최대 (n(n-1)/2)개의 에지가 존재

<br>

### 너비 우선 탐색(BFS)
- 순회 방법
  - 시작 정점으로부터 가까운 정점들을 먼저 방문하고 멀리 있는 정점들은 나중에 방문하는 순회방법
  - 인접한 정점들에 대해서 차례로 다시 너비 우선 탐색을 반복해야 하므로 선입선출의 구조를 갖는 큐를 사용
  ![](https://velog.velcdn.com/images/phwon7/post/1966585d-2e97-4d65-9404-993ad644c763/image.png)

  
- BFS 알고리즘
  - |![](https://velog.velcdn.com/images/phwon7/post/14e6dda9-4752-447f-b3a3-61d8456bfdf8/image.png)|
    |--|
  |![](https://velog.velcdn.com/images/phwon7/post/e94a482f-b67e-4f6d-bd8d-89c98c15d3d6/image.png)|



- BFS의 성능 분석
  - DFS와 같다.
    - 너비우선탐색기법은 그래프의 모든 간선을 조사
    - 인접 리스트로 표현된 경우
      - O(n+e), n은 노드의 수, e는 간선의 수
    - 인접 행렬로 표현된 경우
      - O(n2)
  ![](https://velog.velcdn.com/images/phwon7/post/ca5f5046-d034-42bf-8ebd-5c0fc8e831da/image.png)
    - 희소 행렬인 경우에는 인접 리스트가 훨씬 효과적임을 의미
      - C.f> 최대 (n(n-1)/2)개의 에지가 존재
