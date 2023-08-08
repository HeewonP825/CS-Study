### 신장 트리
#### 신장 트리의 정의
- 그래프 내의 모든 정점을 포함하는 트리
- 모든 정점들이 연결되어 있어야 하고, 사이클을 포함해서는 안된다.
#### 특징과 용도
- n개의 정점을 가지는 그래프의 신장트리는 n-1개의 간선을 가진다.
- 최소의 링크를 사용하는 네트워크 구축 시 사용됨(통신망, 도로망, 유통망 등)
![](https://velog.velcdn.com/images/phwon7/post/4b91a0ca-e4d3-4255-ba06-22ae00483440/image.png)

#### 깊이 우선 신장트리(Defth First Spanning tree)
- 깊이 우선 탐색을 이용하여 생성된 신장 트리
#### 너비 우선 신장트리(Breadth First Spanning tree)
- 너비 우선 탐색을 이용하여 생성된 신장 트리
![](https://velog.velcdn.com/images/phwon7/post/02d50a95-8205-491a-9907-38b4f29e0d3e/image.png)


<br>

### 최소비용 신장트리(MST)
#### 최소비용 신장트리(MST: Minimum cost Spanning Tree)
![](https://velog.velcdn.com/images/phwon7/post/c8d48b81-d64c-4f29-a72e-cc66b953683d/image.png)

- 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 최소인 신장 트리
  -  네트워크에 있는 모든 정점들을 가장 적은 비용으로 연결
- 가중치 그래프의 간선에 주어진 가중치 = 비용/거리/시간 등을 의미하는 값
- MST의 응용
  - 도로건설, 전기 회로 설계, 통신망 구성, 배관 설계 등
- 주어진 그래프에서 최소 신장 트리를 추출하는 알고리즘이 중요하다.
![](https://velog.velcdn.com/images/phwon7/post/4fc0c8b0-8dbe-4c17-b3b8-b549aebcccb9/image.png)

<br>

### Kruskal Algorithm 1)
- **탐욕적 방법(Greedy method) ** 사용
- 가중치가 높은 간선을 제거하면서 MST를 만드는 방법
- 각 단계에서 최선의 답을 선택하는 과정을 반복함으로써 최종적인 해답에 도달한다.
- 탐욕적인 방법이 항상 최적의 해답을 주지는 않는다. 그러나 Kruskal MST Algorithm은 최적의 해답임이 증명되었다.
![](https://velog.velcdn.com/images/phwon7/post/21a27af6-9871-402c-b17e-82d77b0c78c9/image.png)
- Kruskal 알고리즘1을 이용하여 그래프 G의 MST 만들기
![](https://velog.velcdn.com/images/phwon7/post/40c32457-80bb-4581-adb2-fac1caa5ec73/image.png)
![](https://velog.velcdn.com/images/phwon7/post/33f12bb2-07b9-4c35-8420-8595bcca23c8/image.png)

<br>

### Kruskal Algorithm 2)
- **탐욕적 방법(Greedy method) ** 사용
- 가중치가 높은 간선을 삽입하면서 MST를 만드는 방법
![](https://velog.velcdn.com/images/phwon7/post/40a49e80-bfbf-4682-9614-71851cc8e633/image.png)
- 간선을 추가할 때마다 추가하고자 하는 간선이 사이클을 형성하는지를 검사해야 한다.
  - 트리에 간선이 추가되면 싸이클이 생성되기 때문에, 추가하고자 하는 간선이 같은 트리에 속해 있는지 아닌지를 검사한다.(연결 여부 검사)
- 두 정점 a, b를 연결할 때 두 정점이 서로 같은 집합(서로 연결된 그래프)에 속해 있는지, 아닌지를 검사한다.
- Kruskal 알고리즘2를 이용하여 그래프 G의 MST 만들기
![](https://velog.velcdn.com/images/phwon7/post/acae8451-bbb9-4720-bec2-5d029fdafb9a/image.png)
![](https://velog.velcdn.com/images/phwon7/post/a2e15341-84a6-4d42-8d73-9407b6830c8d/image.png)
![](https://velog.velcdn.com/images/phwon7/post/b8b03777-06cd-468b-8238-cd9a9483151a/image.png)

#### union-find 알고리즘
- Kruskal의 MST 알고리즘에서 사이클 검사에 사용
- 두 집합들의 합집합 만들 때 고려중인 정점이 어떤 집합에 속한지를 검사(find연
산)하고, 합하는 연산(union연산)을 수행한다.
- union과 find 연산 등 2개의 연산으로 이루어짐
  - Find 연산
    - 주어진 정점의 루트 노드를 찾아 반환하는 연산
  - Union 연산
    - Find 연산을 이용하여 두 정점의 루트 노드를 찾고
    - 루트 노드가 서로 다르면 두 그래프를 통합
    
#### Kruskal MST Algorithm의 복잡도
- Kruskal 알고리즘은 대부분 간선들을 정렬하는 시간에 좌우된다.
- 사이클 테스트 등의 작업은 정렬에 비해 매우 신속하게 수행된다.
- 네트워크의 간선 e개를 효율적인 알고리즘으로 정렬한다면 Kruskal 알고리즘의 시간 복잡도는 O(e*log(e))가 된다.

<br>

### Prim MST Algorithm
- 시작 정점에서부터 출발하여 신장 트리 집합을 단계적으로 확장해 나감
  - 시작 단계에서는 시작 정점만이 신장 트리 집합에 포함됨
- 신장 트리 집합에 인접한 정점 중에서 최저 가중치 간선으로 연결된 정점을 선택하여 신장트리 집합에 추가
- 이 과정은 신장 트리 집합이 n개의 정점을 가질 때까지 반복
![](https://velog.velcdn.com/images/phwon7/post/ffb6d735-dd06-4408-8c42-765018b406e0/image.png)

![](https://velog.velcdn.com/images/phwon7/post/8cf0d3ef-a8b9-4dfb-85ae-c1c0e32bbdd6/image.png)

![](https://velog.velcdn.com/images/phwon7/post/a8d4069b-076b-40de-8359-24393132e533/image.png)

- 트리 생성 과정은 트리에 이미 포함된 부분그래프와 아직 포함되지 않은 부분 그래프 사이의 최소거리간선을 지속적으로 검사해야 한다.
- 0. 최단거리 리스트를 무한대로 초기화
  - 최단거리리스트: 현재 트리에 포함된 각 노드와 포함되지 않은 노드의 간선 중 최소간선만 갖는 리스트
- 1. 트리 생성 시작
  - 시작 노드를 트리에 포함시키고, 그 노드와 트리에 포함되지 않은 그래프 사이의 거리 중 최단거리를 최단거리리스트에 저장
- 2. 최단 거리리스트 중 최단거리를 선택
- 3. 최단거리를 만드는 노드가 이미 트리에 포함되었는지를 검사하여, 만약 트리에 포함되지 않았으면 그 노드를 트리에 추가
- 4. 트리에 추가된 노드와 아직 포함되지 않는 부분그래프 사이의 최단거리를 최단거리리스트에 저장
- 5. n개의 노드가 모두 트리에 포함될 때까지 2부터 반복

#### Prim MST Algorithm의 복잡도
- 주 반복문이 정점의 수 n만큼 반복하고, 내부 반복문이 2n번 반복하므로 Prim의 알고리즘은 O(n2)의 복잡도를 가진다.

#### MST 알고리즘들의 장단점
- 희박한 그래프: O(e*log(e)) 인 Kruskal의 알고리즘이 유리
- 밀집한 그래프: O(n2) 인 Prim의 알고리즘이 유리

<br>

### 최단 경로(shortest path)
- 네트워크에서 정점 u와 정점 v를 연결하는 경로 중에서 간선들의 가중치 합이 최소가 되는 경로
- 간선의 가중치는 비용, 거리, 시간 등
  - 예) 인접행렬에서 간선이 없는 노드쌍의 가중치는 ∞ 임
        정점 0에서 정점 3으로 가는 최단 경로 문제 : 0,4,1,2,3이 최단 경로
     최단경로 길이는 3+2+4+2=11
     ![](https://velog.velcdn.com/images/phwon7/post/d262db2b-20b1-4024-953d-13659404570f/image.png)
- Dijkstra의 최단경로 알고리즘
![](https://velog.velcdn.com/images/phwon7/post/6af78cc9-ac04-47a1-8625-0c8bdc07b707/image.png)
  - 하나의 시작 정점으로부터 모든 다른 정점까지의 최단 경로 찾음
  - 집합 S
    - 시작 정점 v로부터의 최단경로가 이미 발견된 정점들의 집합
    - 초기에는 시작정점 v만 가짐
  - distance 배열
    - 최단경로가 알려진 정점들만을 이용한 다른 정점들까지의 최단경로 길이
    - distance 배열의 초기값(시작 정점 v)
      - distance[v] = 0
      - 다른 정점에 대한 distance 값은 시작정점 v와 해당 정점간의 가중치 값
    - 매 단계에서 가장 distance 값이 작은 정점을 S에 추가
    <p>
  
 |![](https://velog.velcdn.com/images/phwon7/post/9a5997f8-0586-4fbd-bc9d-38d3bab9f1f2/image.png)|![](https://velog.velcdn.com/images/phwon7/post/d50b9702-59b1-42a9-af34-7bc49855ee7b/image.png)|
 |--|--|
  <p>
  - 새로운 정점이 S에 추가되면 distance값 갱신
 ![](https://velog.velcdn.com/images/phwon7/post/d81b542c-6d1d-4f64-84cc-2f6da7174cfe/image.png)![](https://velog.velcdn.com/images/phwon7/post/b08f3602-6ea3-400d-bac3-83689e0a8f83/image.png)

#### Dijkstra MST Algorithm의 복잡도
- 그래프에 n개의 정점이 있다면, 주반복문을 n번 반복하고 내부 반복문을 2n번 반복하며 O(n2)의 복잡도를 가진다.
