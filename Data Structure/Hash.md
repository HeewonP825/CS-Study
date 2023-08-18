### 해싱(hashing)이란?
* 산술적인 연산을 이용하여 키가 있는 위치를 계산하여 바로 찾아가는 검색방식
* 해싱 함수(hashing function)
  * 키 값을 원소의 위치로 변환하는 함수
* 해시 테이블(hash table)
  * 해싱 함수에 의해서 계산된 주소의 위치에 항목을 저장한 표

#### 탐색 방법
* 탐색키를 입력 받아 해싱함수에 의해 해시 주소 (hash address) 생성
* 이 해시 주소가 배열로 구현된 해시 테이블(hash table)의 인덱스
![](https://velog.velcdn.com/images/phwon7/post/39971aaa-25fc-4507-aee5-263751bfadf6/image.png)

#### 이상적인 해싱
* 회원정보를 해싱으로 저장, 탐색하는 예
  * 전체 회원수가 1000명 이내라고 가정하면 회원번호는 3자리 숫자면 됨
    * 1 김길동
    * 23 김철수
    …
    * 999 홍철수
  * 회원 번호가 23이라면 이 사람의 인적사항은 해시테이블 ht[23]에 저장
    * h(k) = k 로 가정
  * 만약 해시테이블이 1000개의 공간을 가지고 있다면 탐색 시간이 O(1)이 되므로 매우 이상적
  ![](https://velog.velcdn.com/images/phwon7/post/1256229c-ff7e-4559-aa97-6bc1309d2ed8/image.png)
  
<br>

### 실제에서의 해싱
* 실제로는 해시테이블의 크기가 제한되므로, 존재가능한 모든 키에 대해 저장 공간을 할당할 수 없음
* 따라서 주어진 키 값에 대한 적절한 해싱 함수가 필요
* 그러나 해싱 함수에서는 필연적으로 충돌이 발생
  * 해싱 함수를 h(k)= k mod M 이라 하고 M=31 이라고 가정하면 23번과 54번 회원의 키값에서 필연적으로 충돌 발생(위 그림 참고)
  
<br>

### 해시 테이블의 구조 및 용어
* 해시테이블 ht
  * M개의 버켓(bucket)으로 구성된 테이블
  * ht[0], ht[1], ...,ht[M-1]의 원소를 가짐
  * 하나의 버켓에 s개의 슬롯(slot)이 가능
* 충돌(collision)
  * 서로 다른 두 개의 탐색키 k1과 k2에 대하여 h(k1) = h(k2)인 경우
  * 충돌이 발생한 경우에 비어있는 슬롯에 동거자 관계로 키 값 저장
* 오버플로우(overflow)
  * 충돌이 버켓에 할당된 슬롯 수보다 많이 발생하는 것
  * 오버플로우 해결 방법 반드시 필요
  ![](https://velog.velcdn.com/images/phwon7/post/d09b45c8-fbcf-4cd6-aebd-5e11159c050d/image.png)


#### 예시)
* 알파벳 문자열 키의 해시함수가 키의 첫 번째 문자의 순서라고 가정하면
  * h("array")=1
  * h("binary")=2
  …
* 입력데이터: array, binary, bubble, file, digit, direct, zero, bucket 의 저장
![](https://velog.velcdn.com/images/phwon7/post/6079008a-d1ce-452a-9cca-7376651efc2f/image.png)

<br>

### 좋은 해시 함수의 조건
1. 해싱 함수는 충돌이 적어야 한다.
  * 해시 테이블에 고르게 분포되어야 한다.
  * 충돌이 발생하면 같은 버킷을 할당 받는 키 값이 많다는 것을 의미
  * 비어있는 버킷이 많은데도 어떤 버킷은 오버플로우가 발생할 수 있는 상태가 되므로 좋은 해싱 함수가 될 수 없다.

2. 해싱 함수는 계산이 빨라야 한다.
  * 비교 검색 방법을 사용하여 키 값의 비교연산을 수행하는 시간보다 해싱함수를 사용하여 계산하는 시간이 빨라야 해싱 검색을 사용하는 의미가 있다.
  
<br>

### 해싱 함수의 종류
> * 제산 함수
* 폴딩 함수
* 중간 제곱 함수
* 비트 추출 함수
* 승산 함수
* 진법 변환 함수
* 숫자 분석 함수
  …
  
#### 제산 함수
* h(k) = k mod M
* 키 값을 나누는 해시 테이블의 크기 M은 적당한 크기의 소수(prime number)사용
  * 해시 주소가 충돌이 발생하지 않고 고르게 분포하도록 생성되도록 함


#### 폴딩 함수(folding)
* 접지 함수로도 번역
* 키의 비트 수가 해시 테이블 인덱스의 비트 수보다 큰 경우에 사용
  1. 이동 폴딩(shift folding) 함수
    * 각 분할 부분을 이동시켜서 오른쪽 끝자리가 일치하도록 맞추고 더하는 방법
    * 예)해시 테이블 인덱스가 3자리이고, 키 값 k가 12341234123인 경우
    ![](https://velog.velcdn.com/images/phwon7/post/37eae670-de2f-4554-aff0-1ae8d0dcd6fb/image.png)
  2. 경계 폴딩(boundary folding) 함수
    * 분할된 각 경계를 기준으로 접으면서 서로 마주보도록 배치하고 더하는 방법
    * 예)해시 테이블 인덱스가 3자리이고, 키값 k가 12341234123인 경우
    ![](https://velog.velcdn.com/images/phwon7/post/4e5221ab-bfa7-4fce-b88d-194d5d079fe2/image.png)
#### 중간 제곱 함수
* 키 값을 제곱한 다음, 중간에 있는 몇 개의 비트를 주소로 사용
* 제곱한 값의 중간 비트들은 대개 키의 모든 값과 관련이 있다.
* 서로 다른 키 값은 서로 다른 중간 제곱 함수 값을 갖게 된다.
#### 비트 추출 함수
* 해시 테이블의 크기가 2k일 때 키 값을 이진수로 바꾼 다음, 임의의 위치에 있는 k개의 비트들을 추출하여 해시 주소로 사용
#### 승산 함수
* 곱하기 연산을 사용하는 방법
* 키 값 k와 정해진 실수 α를 곱한 결과에서 소수점 이하 부분만을 테이블의 크기 M과 곱하여 그 정수 값을 주소로 사용
#### 진법 변환 함수
* 키 값이 10진수가 아닌 다른 진수일 때, 10진수로 변환하고 해시 테이블 주소로 필요한 자릿수만큼만 하위자리의 수를 사용하는 방법
#### 숫자 분석 함수
* 각 키 값을 적절히 선택한 진수로 변환한 후에 각 자릿수의 분포를 분석하여 가장 편중된 분산을 가진 자릿수는 생략하고, 가장 고르게 분포된 자릿수부터 해시 테이블 주소의 자릿수만큼 차례로 뽑아서 만든 수를 역순으로 바꿔서 주소로 사용
* 예) 키 값이 학번이고 해시 테이블 주소의 자릿수가 3자리인 경우
![](https://velog.velcdn.com/images/phwon7/post/75b8c260-006a-4460-8ed3-3064a4ed2764/image.png)


<br>

### 충돌 해결책
* 충돌(collision)
  * 서로 다른 탐색 키를 갖는 항목들이 같은 해시 주소를 가지는 현상
  * 어떤 해싱 함수도 충돌을 완전히 피하지는 못함
  * 충돌이 발생하면 해시 테이블에 항목 저장 불가능
  * 충돌을 효과적으로 해결하는 방법 반드시 필요
* 충돌해결책
  * 선형조사법: 충돌이 일어난 항목을 해시 테이블의 다른 위치에 저장
  * 체이닝: 각 버켓에 삽입과 삭제가 용이한 연결 리스트 할당
  
#### 선형 조사법(linear probing)
* 알고리즘
  * 해싱 함수로 구한 버킷에 빈 슬롯이 없어서 오버플로우가 발생하면, 그 다음 버킷에 빈 슬롯이 있는지 조사한다.
  
  |해싱함수로 주소값(버킷)을 계산 <br> If 계산된 주소에 빈 슬롯이 있으면 - 키 값을 저장 <br> Else 빈 슬롯이 없으면 - 다시 그 다음 버킷을 조사 <p> 테이블의 끝에 도달하면 다시 테이블의 처음부터 조사 <br> If 조사를 시작했던 시작했던 곳으로 돌아가면 테이블이 가득 찬 것임|
|--|
  
  * 이런 과정을 되풀이 하면서 해시 테이블 내에 비어있는 슬롯을 순차적으로 찾아서 사용하여 오버플로우 문제를 처리하는 방법
  
* 선형 조사법을 이용한 충돌 처리 예
  * 해시 테이블의 크기 : 7
  * 해시 함수 : 제산함수 사용.
    * 해시 함수 h(k) = k mod 7
  * 저장할 키 값 : {8,1,9,6,13}
![](https://velog.velcdn.com/images/phwon7/post/ae214c18-c5d5-448a-bc6b-4265ae794484/image.png)
  
#### 선형조사법(linear probing)의 문제점
* 한번 충돌이 발생하면 충돌이 발생한 위치에 집중적으로 충돌이 발생한다 --> 군집화(Clustering) 현상 발생
* 군집화 현상을 완화시키기 위한 방법
  * 이차 조사법(quardratic probing) 사용
    - 선형조사법과 유사하며 충돌이 발생했을 경우 탐색할 위치를, 일정한 규칙을 이용해 다른 곳을 검사함으로서 군집화 현상을 크게 완화
    - 예)
      * (h(k)+inc*inc) mod M
      * 조사되는 위치 : h(k), h(k)+1, h(k)+4,… 
  * 이중 해싱법(double hashing)
    - 재해싱(rehashing)이라고도 함
    - 오버플로우가 발생하면 원 해시함수와 다른 별개의 해시 함수 사용
      * h(k), h(k)+step, h(k)+2*step, …
      * step=C-(k mod C) (C는 M보다 작은 소수값)
    - 이중 해싱법은 해시 함수값이 같더라도 탐색키가 다르면 서로 다른 조사 순서를 갖기 때문에 집중과 군집화를 피할 수 있다.
* 충돌이 발생한 위치에서 Key값이 삭제되면 연속적인 key값의 조정이 필요하다.
  * 조정하지 않으면 충돌이 발생한 key값은 탐색되지 않는다.
* 거의 모든 버킷이 사용되고 있을 경우에는 탐색 시간이 길어진다.
  
<br>

### 체이닝(chaining)
* 오버플로우 문제를 연결 리스트로 해결
  * 각 버켓에, 삽입과 삭제가 용이한 연결 리스트 할당
  * 버켓 내에서는 연결 리스트 순차 탐색
* (예) 크기가 7인 해시테이블에서 h(k)=k mod 7의 해시 함수 사용
  * 입력 (8, 1, 9, 6, 13) 적용
  ![](https://velog.velcdn.com/images/phwon7/post/fee96ae9-51e3-4a01-b396-151a56836647/image.png)

<br>

  
### 해싱의 성능 분석
|적재 밀도(loading density) 또는 적재 비율(loading factor)|저장되는 항목의 개수 n과 해시 테이블의 크기 M의 비율 <br> ![](https://velog.velcdn.com/images/phwon7/post/498d1311-822c-4ade-be4a-af845daf7298/image.png) <br> a값은 해시테이블이 비어있으면 0, 항목이 버킷의 수만큼 있으면 1|
|--|--|
|<center>선형 조사법에서의 비교 연산 횟수</center>|![](https://velog.velcdn.com/images/phwon7/post/5f7b216b-3f54-4742-9bdd-39818c3f8e5e/image.png)|
|<center>체이닝에서의 비교 연산 횟수</center>|![](https://velog.velcdn.com/images/phwon7/post/243724fb-ef93-4e5c-a18b-27d94b29553e/image.png)|

#### 선형 조사법의 성능 분석
![](https://velog.velcdn.com/images/phwon7/post/ebab9986-f50b-4a60-8182-e691f3730150/image.png)
  * 선형조사법의 적재 밀도 α 가 0.5 이하로 유지해야 탐색 성능을 유지할 수 있다.
  * 이차조사법, 이중해싱법의 경우 적재밀도 α 를 0.7이하로 유지한다.
  * 적재 밀도가 낮을 경우 선형조사법이 더 효율적일 수 있다.

#### 체이닝에서의 비교연산
  * 연결 리스트당 평균적으로 가진 항목의 수를 α라 하면
    * 실패한 탐색: a
    * 성공한 탐색: 1+a/2
  ![](https://velog.velcdn.com/images/phwon7/post/f6426b15-2d4b-4a2a-ad06-f301c1c193b1/image.png)

#### 각 알고리즘에 따른 평균 버켓 접근 수
* 평균적으로 제산 해시 함수를 이용하여 체이닝 기법으로 구현되었을 때 효율이 가장 높다.
![](https://velog.velcdn.com/images/phwon7/post/59a6ba83-5915-455b-a46b-a78876d3bd88/image.png)
#### 해싱과 다른 탐색 방법의 비교
* 평균적으로 균형잡힌 이진탐색트리와 해싱이 가장 좋은 성능을 보인다.
  ![](https://velog.velcdn.com/images/phwon7/post/17324bff-24bd-42de-8151-2ab341d4f0ef/image.png)