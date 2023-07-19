## 1. 스택(Stack)

### 1-1. 스택(Stack)이란?

#### 1-1-1) 스택의 기본 개념

+ 스택이란 **선형적 자료구조**로 한쪽끝은 **top**, 다른쪽 끝은 **bottom**이라 부르며 추가적인 삽입과 삭제는 top에서만 가능한 자료구조 이다.
+ 스택은 또한 **LIFO(Last In First Out)** 구조로, 가장 나중에 들어간 데이터가 제일 먼저 나가는 구조이다.
![](https://velog.velcdn.com/images/phwon7/post/114d91e7-c1f9-4271-8732-faffd58143bf/image.png)

<br>

#### 1-1-2) 시스템 스택(System Stack)
- **시스템 스택(system stack)** 은 운영체제가 사용하는 스택이다.

- 함수의 실행이 끝나면 자신을 호출한 함수로 되돌아가야 하는데 이 때 복귀할 주소를 기억하는 데 스택이 사용된다.
  
  - 함수는 호출된 역순으로 되돌아가야 하기 때문이다.
  ![](https://velog.velcdn.com/images/phwon7/post/7bae6710-8267-4442-ac69-343a34523405/image.png)
  - 함수가 호출될 때마다 프로그램은 활성화 레코드 또는 스택 프레임이라고 하는 구조를 만들고 시스템 스택의 맨 위에 놓는다.
  - 프레임 포인터(fp)는 현재 스택 프레임에 대한 포인터이며 시스템은 또한 스택 포인터(sp)를 별도로 유지 관리한다.

<br>

### 1-2. 코드로 보는 스택

#### 1-2-1) C에서의 스택
- ADT로 보는 스택
![](https://velog.velcdn.com/images/phwon7/post/d95f0378-f31f-43f5-ac78-431ddfbc80f9/image.png)

<br>

- C에서 스택 생성은 1D 배열(1차원 배열)을 사용하여 스택을 나타내며 스택 요소는 스택[0]에서 스택[top]까지 저장된다.

|CreateS()|![](https://velog.velcdn.com/images/phwon7/post/d006c12b-105c-451a-bde8-cd36d70c9427/image.png)|
|--|--|
|<center> **push()** </center>|![](https://velog.velcdn.com/images/phwon7/post/377c091f-691f-41b7-8b94-81f1d77e24c9/image.png)|
|<center> **pop()** </center>|![](https://velog.velcdn.com/images/phwon7/post/4f164875-48ca-4580-90e9-302d26c7c4e8/image.png)|
|<center> **stackFull()** </center>|![](https://velog.velcdn.com/images/phwon7/post/d5394c4a-0ebe-464e-b463-bda06bbb685c/image.png)|

<br>

#### 1-2-2) 동적 할당 배열을 사용하는 스택

|<center> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CreateS() <br> IsEmpty() <br> IsFull()</center>|![](https://velog.velcdn.com/images/phwon7/post/b5eefedb-4b26-43df-8434-f4bae1f34625/image.png)|
|--|--|
|<center> **pop()** </center>|![](https://velog.velcdn.com/images/phwon7/post/4f164875-48ca-4580-90e9-302d26c7c4e8/image.png)|
|<center> &nbsp;**stackFull()** </center>|![](https://velog.velcdn.com/images/phwon7/post/0b5a2f63-6dd1-48f6-8c47-a584f35cd944/image.png)|

<br>

## 2. 큐(Queue)

### 2-1. 큐(Queue)란?
- **큐(Queue)**는 선형 자료구조로 한쪽 끝은 **front**, 다른쪽 끝은 **rear** 라고 부르며 삽입은 오직 rear쪽에서만 가능하고 삭제는 front에서만 가능한 자료구조이다. 
- 큐는 FIFO(First In First Out) 자료구조로 먼저 들어간 데이터가 먼저 나오는 순입순차의 구조를 갖고 있다.
![](https://velog.velcdn.com/images/phwon7/post/c174ae70-1221-490a-8ec2-03c1cc70be6e/image.png)

<br>

### 2-2. 코드로 보는 큐

#### 2-2-1) C에서의 큐
- ADT로 보는 큐
![](https://velog.velcdn.com/images/phwon7/post/b9bdf1f3-efb4-4fb5-b318-9590149fcee6/image.png)
- 순차 표현은 스택과 마찬가지로 1D 배열을 사용하지만, 큐는 원형 표현(원형 큐)또한 가능한데 이때도 똑같이 1D 배열을 사용한다. 원형큐는 선형큐에 비해 효율성이 향상된다고 말할 수 있다.
- ![](https://velog.velcdn.com/images/phwon7/post/88b6f70f-f02d-44e3-9ed7-c74dc594c2e7/image.png)

|<center> 큐 생성 함수 CreateQ() </center>|![](https://velog.velcdn.com/images/phwon7/post/40bed06b-d5a6-40b1-9a5e-cb5ad5b37a51/image.png)
|--|--|
|<center> **addq() <br> 함수** </center>|![](https://velog.velcdn.com/images/phwon7/post/bca89ce5-77df-4ba6-a22f-b097cf16eac7/image.png)|
|<center> **deleteq() 함수** </center>|![](https://velog.velcdn.com/images/phwon7/post/41737631-dc3c-40b6-ba9b-ba4a8852d2bf/image.png)|
|<center> **addq(), deleteq() 예시** </center>|![](https://velog.velcdn.com/images/phwon7/post/704ccbb5-81ee-4887-9ba7-f8d523cbe754/image.png)|

- 예시) OS의 Job Scheduling
- ![](https://velog.velcdn.com/images/phwon7/post/82623fd4-e117-415e-a3ab-0dbd0881a055/image.png)
- queueFull
  - array shifting : time-consuming, Worst case time complexity, O(MAX_QUEUE_SIZE)
  ![](https://velog.velcdn.com/images/phwon7/post/7f1331fc-3a22-4bb4-95c5-bd5ee157be4a/image.png)

<br>

#### 2-2-2) 원형 큐
- **원형 큐(Circular Queue)**는 1D 배열을 사용하는 큐로 원형 구조의 1D 배열을 사용한다.

|![](https://velog.velcdn.com/images/phwon7/post/c6b41326-fe9d-416a-b331-5dce5c4e9d93/image.png)|![](https://velog.velcdn.com/images/phwon7/post/89bf98ec-f050-4def-a6a0-e72f4c7344b7/image.png)|
|--|--|
|<center> **일반적인 선형 큐(Linear Queue)** </center>|<center> **원형 큐(Circular Queue)** </center>|

- front와 rear에는 정수 타입 변수를 사용한다.
  - front는 첫 번째 요소에서 시계 반대 방향으로 한 위치이다.
  - rear는 마지막 요소의 위치를 제공한다.
![](https://velog.velcdn.com/images/phwon7/post/cdb6506c-7aff-43af-b359-9b293ff9500c/image.png)

- 원형큐에 요소를 삽입할 때는 rear를 시계방향으로 한 번 이동 시키고 queue[rear]에 집어 넣는다.

|![](https://velog.velcdn.com/images/phwon7/post/f6cd7c00-82f2-4769-86f3-208757efa554/image.png)|![](https://velog.velcdn.com/images/phwon7/post/a0e546fa-4009-46dd-9648-72a433da337d/image.png)![](https://velog.velcdn.com/images/phwon7/post/4d773080-5123-4699-90e9-8eb3dda9373a/image.png)|
|--|--|
- 원형큐에 요소를 삭제할 때는 front를 시계방향으로 한 번 이동 시키고 queue[rear]에서 제거한다.

|![](https://velog.velcdn.com/images/phwon7/post/6dd563c7-1d0f-4fdc-9673-15fbb819604f/image.png)|![](https://velog.velcdn.com/images/phwon7/post/e38ccc3f-4190-421c-8af5-e8e7ab979d45/image.png)![](https://velog.velcdn.com/images/phwon7/post/da331f0c-5c06-44ed-9d29-f5f3fe874657/image.png)|
|--|--|

<br>
<br>
<br>
<br>
<br>

*_추가적으로 동적할당 스택, 큐 & array doubling 시간복잡도 재정리 필요_

### 참조)
- https://roi-data.com/entry/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-4-%EC%8A%A4%ED%83%9DStack%EC%9D%B4%EB%9E%80-%EC%97%B0%EC%82%B0-%EA%B5%AC%ED%98%84%EB%B0%A9%EB%B2%95
- 자료구조, data structure, Horowitz, Shani, & Anderson-Freed, ªFundamentals of data structures in Cª, (2nd edition) Silicon-press. 강의자료 ppt

<br>

### 원문)
- [https://velog.io/@phwon7/자료구조-스택Stack과-큐Queue-1](https://velog.io/@phwon7/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue-1)
