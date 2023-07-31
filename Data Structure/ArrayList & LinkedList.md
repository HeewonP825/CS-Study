### 배열과 연결리스트의 차이

|Sequential Representation|Linked Representation|
|--|--|
| 순차 저장 방식 <br> 목록의 연속적인 항목은 고정된 거리만큼 떨어져있다 <br> 요소의 순서가 요구된 목록과 동일하다 <br> 임의 요소의 삽입 및 삭제에 많은 비용이 소요된다 <br> 과도한 데이터 이동이 있을 수 있다|목록에서 연속된 요소는 메모리의 어디에나 배치될 수 있다 <br> 요소의 순서가 순서 목록과 같을 필요는 없다 <br> 연결된 목록은 노드로 구성된다 <br> 각 노드에 0 이상의 데이터 필드와 다음 요소에 대한 하나 이상의 링크 또는 포인터 필드가 있다 <br> 임의 요소의 삽입 및 삭제가 더 쉬워진다 <br> 데이터의 이동이 없다|

![](https://velog.velcdn.com/images/phwon7/post/2b1e2393-6a07-4b57-b721-2dc5ec8f18c9/image.png)
- 단일연결리스트에서 각 노드에는 포인터 필드가 하나씩만 있다.
- 체인은 0개 이상의 노드로 구성된 단일연결리스트를 말한다.

<br>

### 연결리스트 - 삽입(Insert)
![](https://velog.velcdn.com/images/phwon7/post/bd7c9c08-4bed-4c21-af30-2a33e0e2c1d5/image.png)

![](https://velog.velcdn.com/images/phwon7/post/443e4adf-cc43-4031-9c31-1ea7d97b7c28/image.png)

<br>

### 연결리스트 - 삭제(delete)
![](https://velog.velcdn.com/images/phwon7/post/9ea00c74-4050-480c-9444-86bbe548e888/image.png)

![](https://velog.velcdn.com/images/phwon7/post/e0f58a86-f0f9-4105-a68d-6f2b034ab03b/image.png)

<br>

### C에서의 단일연결리스트
![](https://velog.velcdn.com/images/phwon7/post/dc572e49-8a8e-4f8c-97db-f031aad9d2e2/image.png)

![](https://velog.velcdn.com/images/phwon7/post/3f1d7d22-f1a5-4d7d-92d4-2abba2acd664/image.png)

#### 리스트 삽입(List Insertion)

|![](https://velog.velcdn.com/images/phwon7/post/35dac5e5-47e8-4a79-8c5d-60342053a5d2/image.png)|
|--|
|![](https://velog.velcdn.com/images/phwon7/post/6465f2e7-9913-4d71-9e8b-39aa05862ab8/image.png)|
|![](https://velog.velcdn.com/images/phwon7/post/86b7d0bb-a7aa-4f15-9011-0df3510c8b43/image.png)|

#### 리스트 삭제(List Deletion)
|![](https://velog.velcdn.com/images/phwon7/post/3e837164-cda7-4b87-9eff-27a1869e787c/image.png)|
|--|
|![](https://velog.velcdn.com/images/phwon7/post/7c3490c4-edcb-4d2b-9135-56abeacf98a0/image.png)|

#### 리스트 출력(List Print)
![](https://velog.velcdn.com/images/phwon7/post/d3e1c1a5-83dd-410c-a2a5-860646d6b006/image.png)

### 다항식 표현(Polynominal Represenation)
- 다항식(Polynominal)
![](https://velog.velcdn.com/images/phwon7/post/d297a81f-12dd-475d-94ef-bd0e9fd77e4e/image.png)
  - ai: 0이 아닌 것.
  - E: 음의 적분 지수.


- 다항식의 표현
![](https://velog.velcdn.com/images/phwon7/post/eb17e427-8cc3-410e-8ecb-50df0b781481/image.png)

|![](https://velog.velcdn.com/images/phwon7/post/ac8243ed-6690-4489-9c0e-69868973f234/image.png)|![](https://velog.velcdn.com/images/phwon7/post/9fa82314-723c-4199-b2fb-9095e0ee79be/image.png)
|--|--|

- C에서의 다항식

|padd()|![](https://velog.velcdn.com/images/phwon7/post/7960bb48-ea2a-4ece-ad31-1131b1a3cec1/image.png)|
|--|--|
|**attatch()**|![](https://velog.velcdn.com/images/phwon7/post/27bed515-6496-409e-847e-46932697f47f/image.png)|
|<center> **erase()** </center>|![](https://velog.velcdn.com/images/phwon7/post/230efcc3-a485-4b66-bcec-5c8eb856e23b/image.png)


- Analysis padd()
  - 이 알고리즘의 세가지 비용 측청치
    1. 계수 추가
    ![](https://velog.velcdn.com/images/phwon7/post/e95b1da7-e253-4d3e-a054-ef5128176144/image.png)
    0 ≤ 계수 추가 횟수 ≤ min{m, n}
    
    2. 지수 비교
      - While 루프의 각 반복에 대한 한 번의 비교
      - 반복 횟수는 m + n으로 제한된다.
        ex) m+n-1 반복: 식 = n 및 ![](https://velog.velcdn.com/images/phwon7/post/789ebe0e-8e45-4f4e-a85a-9e0b998c1a04/image.png)
        
    3. c에 대한 새 노드 생성
      - c의 최대 항 수는 m + n입니다

=> (1)부터 (3)까지, 총 시간 복잡도는 **O(m + n)** 이다.

### 이중 연결 리스트(Double Linked List)

- 단순 연결 리스트(chain)의 문제점
  - 선행 노드를 찾기가 힘들다
    -> 특정 노드 p 또는 노드 p 앞에 있는 노드를 찾는 유일한 방법은 목록의 처음부터 시작하는 것 뿐이다.
  - 삽입이나 삭제시에는 반드시 선행 노드가 필요하다


- 이중 연결 리스트는 하나의 노드가 선행 노드와 후속 노드에 대한 두개의 링크를 가지는 리스트로, **링크가 양방향** 이므로 **양방향 검색이 가능** 하다. 그러나 공간을 많이 차지하며 코드가 비교적 복잡하다는 단점이 있다.
- 실제 사용되는 이중 연결 리스트의 형태: 헤드 노드 + 이중 연결 리스트 + 원형 연결 리스트
![](https://velog.velcdn.com/images/phwon7/post/1ef74456-d88a-4535-a022-175c47cd43ef/image.png)
  - 헤드 노드(head node): 데이터를 가지지 않고 단지 삽입, 삭제 코드를 간단하게 할 목적으로 만들어진 노드. 헤드 포인터와의 구별이 필요하며 공백 상태에서는 헤드 노드만 존재한다.
  
<br>  

|이중 연결 리스트에서의 노드의 구조|![](https://velog.velcdn.com/images/phwon7/post/a8e04c18-b960-44c2-a6d7-a73b51b35ac8/image.png)|
|--|--|

- ptr이 이중으로 연결된 목록의 임의의 노드를 가리키면
  ptr = ptr->llink->rlink = ptr->rlink->link 이 공식을 반영한다.
- 이 공식은 우리가 앞 뒤 똑같은 난이도로 접근할 수 있다는 사실을 알려준다.
![](https://velog.velcdn.com/images/phwon7/post/5f68be6b-1139-484e-bcb6-eeedc110b882/image.png)

<br>

#### 삽입 연산(Dinsert())

|![](https://velog.velcdn.com/images/phwon7/post/e7c53ed3-7029-4d13-82d0-b1a8f54c38ba/image.png) <br> ![](https://velog.velcdn.com/images/phwon7/post/1f177bde-bdb0-474e-8baa-d885f0e96374/image.png)|
|--|

<br>

#### 삭제 연산(Ddelete())

|![](https://velog.velcdn.com/images/phwon7/post/e0c9a3cd-b90a-45c9-b036-b8eda91fd5ac/image.png)![](https://velog.velcdn.com/images/phwon7/post/43ae24f0-18bb-4e31-8066-be6172ec4194/image.png)![](https://velog.velcdn.com/images/phwon7/post/284d0e7a-2c6e-47e9-832c-8e0b77bfc78b/image.png)|
|--|

