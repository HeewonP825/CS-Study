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
