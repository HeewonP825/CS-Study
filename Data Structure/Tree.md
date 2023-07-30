### 트리의 정의
- 트리는 싸이클을 갖지 않는 연결된 그래프이며 하나 이상의 유한 집합이다.
- Rooted Tree를 트리라고 한다.(루트라고 하는 특별히 지정된 노드가 있다)
- 루트 노드를 제외한 나머지 노드는 n≥0으로 분할된다.
  - 분리된 집합 T1, …, Tn, 여기서 이들 각각의 집합은 a라고 할 때, T1,…, Tn을 뿌리의 하위 트리(subtrees)라고 부른다.
![](https://velog.velcdn.com/images/phwon7/post/89658c42-760c-431c-b809-9fd79ee049b0/image.png)

<br>
  
### 트리의 응용 분야
- 계층적인 조직표현을 할 때 거의 필수적으로 사용 됨.
- 컴퓨터 디스크의 디렉토리 구조
- 인공지능에서의 결정트리(decision Tree)
- 데이터 관리를 위한 도구

### 트리 용어 설명
![](https://velog.velcdn.com/images/phwon7/post/7690e7cf-921c-452e-be0e-ee80b7d34cd0/image.png)

|용어 이름|설명|
|--|--|
|노드(node)|트리의 구성 기본 요소|
|간선(edge)|노드와 노드를 연결하는 선|
|차수(degree)|- 노드가 가지고 있는 자식 노드의 개수(노드의 하위 트리(subtrees) 수) <br> - 트리의 차수: 트리에 있는 노드의 최대 차수|
|하위 트리(subtrees)|자식 노드와 그 자식 노드의 자손들로 이루어진 트리|
|리프(leaf)|- 단자 노드(terminal node), 차수가 0인 노드 <br> - <반대> 비단말 노드: 적어도 하나의 자식을 가지는 노드|
|루트(root)|- 부모가 없는 노드 <br> - 부모, 자식, 형제, 조상, 자손 노드: 인간과 동일하게 생각하면 됨 <br> - 조상: 루트에서 노드까지 가는 경로를 따라 있는 모든 노드 <br> - 자손: 하위 트리에 있는 모든 노드|
|레벨(level)|트리 각 층의 번호|
|높이(height)|트리의 최대 레벨|


### 리스트 표현

"(A (B (E (K, L), F), C (G), D( H (M), I, J) ) )"

|![](https://velog.velcdn.com/images/phwon7/post/7433c04b-4703-430f-ad45-13b51a637435/image.png)|![](https://velog.velcdn.com/images/phwon7/post/9372b9c3-a1a9-4a34-9f80-9fb7f9a5329e/image.png)|
|--|--|

<br>

#### Left Child-Right Sibling Representation as a Degree Two Trees

|![](https://velog.velcdn.com/images/phwon7/post/b887dffd-f9fa-42ec-a46b-26bcf2d39da4/image.png)|![](https://velog.velcdn.com/images/phwon7/post/287aea82-e45d-496f-913e-298f369e383a/image.png)|
|--|--|
|![](https://velog.velcdn.com/images/phwon7/post/1839b1ad-7454-425e-a055-4b1bff38fe84/image.png)|![](https://velog.velcdn.com/images/phwon7/post/64e95cc0-15ac-4faa-966d-11530b6a6e82/image.png)![](https://velog.velcdn.com/images/phwon7/post/a68d800e-6c61-41d0-b0c0-e1c5b74e6cc2/image.png)|

![](https://velog.velcdn.com/images/phwon7/post/d081ca73-ba82-4e2a-8268-66c75c57ec94/image.png)

<br>

### 이진 트리(Binary Tree)

- 트리는 크게 이진트리와 일반트리로 나눌 수 있다.
  - 일반 트리와 이진 트리는 노드가 0인 트리는 없지만 빈 이진 트리가 있고, 자식들(서브 트리) 간의 순서가 존재한다는 점이 다르다.
  - |![](https://velog.velcdn.com/images/phwon7/post/7a480d8d-961a-4eec-8e53-3e6893cba988/image.png)|![](https://velog.velcdn.com/images/phwon7/post/9a39f185-a502-47e9-88f6-da03c386d043/image.png)|
  |--|--|
- 이진 트리(binary Tree)는 모든 노드가 최대 2개의 서브 트리를 가지고 있는 트리이다.
- 이때, 서브 트리는 공집합일 수 있으며, 모든 노드의 차수가 2 이하가 된다
  - -> 이러한 점에서 구현하기 편리함
- 이진 트리에는 서브 트리간의 순서가 존재한다.
- 이진 트리의 노드의 개수가 n개이면 간선의 개수는 n-1이다.

![](https://velog.velcdn.com/images/phwon7/post/52634541-0024-4c94-ba28-afeff20e7661/image.png)

![](https://velog.velcdn.com/images/phwon7/post/a6524720-90ab-4db1-9f85-f033ad125ed4/image.png)

#### 이진 트리의 성질

|Properties of Binary Trees |
|--|
|<center><br>**높이가 h인 이진트리에서 노드의 개수 <br> - 최소 h개의 노드 <br> - 최대 2h-1개의 노드**</ccenter>|
|![](https://velog.velcdn.com/images/phwon7/post/3d5881e5-452a-448d-b59a-bd261f16e5e8/image.png)|
|<center>**n개의 노드를 가지는 이진트리의 높이 <br> - 최대 n <br> - 최소 log2(n+1)**</center>|
|![](https://velog.velcdn.com/images/phwon7/post/f1a1e1bb-6c7d-4806-a2fc-7c0306bce793/image.png)|

<br>

#### 이진 트리의 분류

![](https://velog.velcdn.com/images/phwon7/post/86f2d94c-331a-441c-8150-d7ea241dfc2d/image.png)

- 포화 이진 트리(full binary tree)
  - 트리의 각 레벨에 노드가 꽉 차있는 이진트리.
  ![](https://velog.velcdn.com/images/phwon7/post/2545a940-41ab-448a-b7cc-6896410c75b4/image.png)
  - 포화 이진 트리에는 다음과 같이 각 노드에 번호를 붙일 수 있다.
  ![](https://velog.velcdn.com/images/phwon7/post/6f96b61a-f70d-475c-9840-6a423b247e46/image.png)
  
<br>

- 완전 이진 트리(complete binary tree)
  - 레벨 1부터 k-1까지는 노드가 모두 채워져 있고, 마지막 레벨 k에서는 왼쪽부터 오른쪽으로 노드가 순서대로 채워져 있는 이진트리
  - 포화 이진 트리와 노드 번호가 일치한다.
  ![](https://velog.velcdn.com/images/phwon7/post/74b4fdf3-702e-4290-b31f-573fa47efbcc/image.png)
  
- 포화 이진 트리 vs 완전 이진 트리
  - ||포화 이진 트리|완전 이진 트리|
    |--|--|--|
    |정의|- 모든 레벨이 채워져있는 이진트리 <br> - 노드로 완전히 채워진다 <br> - 마지막 레벨의 노드는 왼쪽에서 오른쪽으로<br>(순차적인 방식) <br>|- 모든 레벨이 채워져있는 이진트리 <br> - 노드로 완전히 채워진다 <br> - 마지막 레벨의 노드는 왼쪽에서 오른쪽으로<br>(순차적인 방식) <br> **그러나 일부 빈 공간이 있을 수 있다**|
    |노드 개수|N = 2k-1|N = 2k-1|
    |빈 공간|- 모든 레벨이 꽉 찼으므로 빈 공간이 없다|- 빈 공간이 있을 수 있다. <br> - 마지막 레벨의 오른쪽에서만 생길 수 있다|

<br>

### 이진 트리의 표현법
- 이진 트리의 표현에는 배열을 이용하는 방법과 포인터를 이용하는 방법이 있다.

#### 1. 배열 표현법
- 모든 이진 트리를 포화 이진 트리라고 가정한 뒤, 루트 노드를 1번으로 시작하혀 각 노드에 번호를 붙이고 그 번호를 배열의 인덱스로 사용한다.
- 노드가 있으면 데이터를 저장하고 노드가 없으면 null값을 저장한다.

|![](https://velog.velcdn.com/images/phwon7/post/895ab055-75ad-4de7-ba66-b30702ead1d3/image.png)|
|--|
|![](https://velog.velcdn.com/images/phwon7/post/709e8a42-a62f-48f4-8cfb-d74f8003d6ab/image.png)|
|![](https://velog.velcdn.com/images/phwon7/post/b3f8d97d-a063-416c-aa60-4488de320fe3/image.png)|

- 노드 i의 부모 노드 인덱스는 어떻게 계산할까?-> i/2
- 노드 i의 왼쪽 자식 노드 인덱스는? -> 2i
- 노드 i의 오른쪽 자식 노드 인덱스? -> 2i + 1


#### 2. 링크 표현법
- 노드를 포인터를 포함하는 구조체로 정의한다.
- 포인터를 이용하여 간선(edge)를 포함한다.
  - 노드는 구조체, 링크는 포인터로 표현

|![](https://velog.velcdn.com/images/phwon7/post/8d890a32-a7d2-48c6-a25d-8410d7f9f7d3/image.png)|
|--|
|![](https://velog.velcdn.com/images/phwon7/post/fe9bd044-5e98-4dd1-8881-ef992934a0b4/image.png)|
|![](https://velog.velcdn.com/images/phwon7/post/2d2a7917-eb05-4c2d-a8f2-166c61c72406/image.png)|

<br>

### 이진 트리의 순회(Binary Tree Travesal)

- 트리 순회: 트리의 각 노드를 한 번만 방문하는 것
- 이진 트리를 횡단할 때,
  - L, V, R: 왼쪽 이동, 노드 방문, 오른쪽 이동
- 횡단에 가능한 6가지 조합
  - LVR, LRV, VLR, VRL, RVL, RLV
- 왼쪽을 오른쪽보다 먼저 순회한다면 세가지가 남는다.
  - LVR: inorder
  - LRV: postorder
  - VLR: preorder


- 이는 각각 infix, postfix, prefix와 유사한 점이 존재한다. 
- A/B*c*d+E의 다항식을 이진 트리로 고려해 본다면, 연산자를 포함하는 각 노드에 대해
  - 왼쪽 하위 트리는 왼쪽 피연산자
  - 오른쪽 하위 트리 오른쪽 피연산자로 나눌 수 있다.
  ![](https://velog.velcdn.com/images/phwon7/post/b1adc498-51f9-4a9f-818e-8c4e6ef07ff5/image.png)
  
