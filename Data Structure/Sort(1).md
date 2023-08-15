### 정렬이란?
* 객체를 크기순으로 오름차순이나 내림차순으로 나열하는 것.
* 자료 탐색에 있어서 필수적이다.
* 일반적으로 정렬시켜야 될 대상을 레코드(record)라고 부른다.
  * 레코드는 한 개 이상의 필드(feild)로 이루어져있고, 다른 레코드와 구별하기 위한 필드를 키(key) 필드라고 한다.
  ![](https://velog.velcdn.com/images/phwon7/post/e7a9897b-1333-4411-9636-7ef56a772de5/image.png)
  
* 모든 경우에 최적인 정렬 알고리즘은 없으며, 각 응용 분야에 적합한 정렬 방법을 사용해야 한다.
  * 레코드 수의 많고 적음 / 레코드 크기의 크고 작음
  * Key의 특성(문자, 정수, 실수 등)
  * 메모리 내부/외부 정렬


* |단순하지만 비효율적인 방법|복잡하지만 효율적인 방법|정렬 알고리즘의 안정성|
|--|--|--|
| <center> 삽입정렬(insertion sort) <p> 선택정렬(selection sort) <p> 버블정렬(bubble sort)</center>|<center>퀵정렬(quick sort) <p> 히프정렬(heap sort) <p>합병정렬(merge sort) <p> 기수정렬(radix sort)</center>|<center>동일한 키 값을 갖는 레코드들의 <p>상대적인 위치가 <p> 정렬 후에도 바뀌지 않음</center>|

<br>

### 선택 정렬(Selection Sort)

* 정렬된 왼쪽 리스트와 정렬 안된 오른쪽 리스트 가정
  * 초기에는 왼쪽 리스트는 비어 있고, 정렬할 숫자들은 모두 오른쪽 리스트에 존재
* 오른쪽 리스트에서 최소값 선택하여 오른쪽 리스트의 첫번 째 수와 교환
  * 왼쪽 리스트 크기 1 증가
  * 오른쪽 리스트 크기 1 감소
  * 오른쪽 리스트가 소진되면 정렬 완료
  ![](https://velog.velcdn.com/images/phwon7/post/47ff567e-2925-49ab-b241-263a6b3b6443/image.png)
* 유사 코드
![](https://velog.velcdn.com/images/phwon7/post/dedafd9c-17e2-4a1e-83b2-a5610b7e2787/image.png)
* 선택 정렬 소스 코드 
```
#define SWAP(x, y, t) ( (t)=(x), (x)=(y), (y)=(t) )

void selection_sort(int list[], int n) {
	int i, j, least, temp;
    
	for(i=0; i<n-1; i++) {
		least = i;
		for( j=i+1; j<n; j++)
			if(list[ j]<list[least]) least = j; // 최소값 탐색
		SWAP(list[i], list[least], temp);
	}
}
```
* 선택 정렬 복잡도 분석
  * 비교 횟수 : (n - 1) + (n - 2) + … + 1 = n(n - 1)/2 = O(n2)
  * 이동 횟수 : 3(n - 1)
  * 전체 시간적 복잡도: O(n2)
  * 안정성을 만족하지 못함

<br>

### 삽입 정렬(Insertion Sort)
* 정렬되어 있는 부분 집합에 정렬할 원소의 위치를 찾아 삽입하는 방법

|![](https://velog.velcdn.com/images/phwon7/post/aa194cf5-3ee1-4ea8-bb02-15ed5610290c/image.png)|![](https://velog.velcdn.com/images/phwon7/post/65bb24e9-a875-419f-9566-442353a6072e/image.png)
|--|--|

* 삽입 정렬 알고리즘
  1. 두 번째 원소(인덱스 i=1)부터 시작
  2. i번째 값을 key로 복사
  3. 정렬된 배열의 적당한 위치에 key 삽입
     1) j를 정렬된 배열을 역순부터 조사하기 위한 첨자라고 하면, j = i-1로 초기화
     2) key 값보다 정렬된 배열의 j번째 값이 크면 j번째를 j+1번째로 이동
     3) j를 하나 감소하여 2) ~ 3)과정 반복
     4) j번째 정수가 key보다 작거나, j 값이 음수면 j+1위치에 key 삽입
  4. i를 1 증가, i번째 원소를 key로 함
  5. 2~4 과정을 마지막 원소까지 반복
  ![](https://velog.velcdn.com/images/phwon7/post/37ac4288-0ea6-4ed9-9c6f-39a2a3f3fcfc/image.png)
* 삽입 정렬 소스 코드
```
// 삽입정렬
void insertion_sort(int list[], int n) {
	int i, j, key;
	for(i=1; i<n; i++){
		key = list[i];
		for( j=i-1 ; j>=0 && list[ j]>key ; j--)
			list[ j+1] = list[ j]; // 레코드의 오른쪽 이동
			list[ j+1] = key;
		}
	}
```

* 삽입 정렬 분석
  * 계산 복잡도
    * 최선의 경우 O(n) : 이미 정렬되어 있는 경우
      * 비교: n-1 번  O(n)
      * 이동: 2(n-1) 번  O(n)
    * 최악의 경우 O(n2) : 역순으로 정렬되어 있는 경우
      * 모든 단계에서 앞에 놓인 자료 전부 이동
      * 전체 비교 횟수: O(n2)
      * 이동: O(n2)
    * 평균의 경우 O(n2)
  * 특징
    * 많은 이동 필요 -> 레코드가 클 경우 불리
    * 안정된 정렬방법
    * 대부분 정렬되어 있으면 매우 효율적
    
<br>

### 셸 정렬(Shell Sort)
* 삽입정렬이 어느 정도 정렬된 리스트에서 대단히 빠른 것에 착안되어 만들어졌다.
* 삽입 정렬은 요소들이 이웃한 위치로만 이동하므로, 많은 이동에 의해서만 요소가 제자리를 찾아간다.
* 요소들이 멀리 떨어진 위치로 이동할 수 있게 하면, 보다 적게 이동하여 제자리 찾을 수 있다.
* 셸 정렬의 알고리즘
  1. 전체 리스트를 일정 간격(gap, interval)의 부분 리스트로 나눔(일반적으로 배열 크기의 1/2의 간격)
  2. 나뉘어진 각각의 부분 리스트를 삽입정렬
  3. 간격을 줄인 부분 리스트를 만들어 부분 리스트의 수는 줄이고, 각 부분 리스트의 크기는 더 커지게 하여 간격이 1이 될 때까지 부분 리스트에 대하여 1, 2, 과정 과정 반복

|정렬되지 않은 {69, 10, 30, 2, 16, 8, 31, 22}의 <br> 자료들을 셸 정렬|
|--|--|
|<center>원소의 개수가 8개이므로 간격 gap은 4에서 시작 <br> gap=4 이므로 간격이 4인 원소들을 같은 부분 집합으로 만들면 4개의 부분 집합이 만들어진다</center>|![](https://velog.velcdn.com/images/phwon7/post/55676031-7a35-48db-a41c-871d2fb930b7/image.png)
|<center>첫 번째 부분 집합 {69, 16}에 대해서 삽입 정렬을 수행하여 정렬.</center>|![](https://velog.velcdn.com/images/phwon7/post/87769c96-0e15-478d-8391-4e438dcd7e17/image.png)
|<center>두 번째 부분 집합 {10, 8}에 대해서 삽입 정렬 수행</center>|![](https://velog.velcdn.com/images/phwon7/post/fb43c297-ed14-451a-8a98-0633d685c0a6/image.png)|
|<center>세 번째 부분 집합 {30, 31}에 대해서 삽입 정렬을 수행하는데, (30<31) 이므로 자리 교환은 이루어지지 않는다.</center>|![](https://velog.velcdn.com/images/phwon7/post/f0559197-34a5-4065-a438-332faaac1146/image.png)
|<center>네 번째 부분 집합 {2, 22}에 대해서 삽입 정렬을 수행하는데,(2<22) 이므로 자리 교환은 이루어지지 않는다</center>|![](https://velog.velcdn.com/images/phwon7/post/cf494cc7-cb8e-4590-a564-0df81dd06c7b/image.png)|
|<center>gap을 2로 변경하고 다시 셸 정렬 시작.<br> gap=2 이므로 간격이 2인 원소들을 같은 부분 집합으로 만들면 2개의 부분 집합이 만들어진다.</center>|![](https://velog.velcdn.com/images/phwon7/post/f7d4fb5f-3de9-447d-9607-895448d6af34/image.png)
|<center>첫 번째 부분 집합 {16, 30, 69, 31}에 대해서 삽입 정렬을 수행하여 정렬</center>|![](https://velog.velcdn.com/images/phwon7/post/da2f93f5-0c4d-48da-82f0-033fcf8ba483/image.png)|
|<center>두 번째 부분 집합 {8, 2, 10, 22}에 대해서 삽입 정렬을 수행하여 정렬</center>|![](https://velog.velcdn.com/images/phwon7/post/246dfee8-5a28-4209-8247-5201f26808df/image.png)
* 셸 정렬 소스코드
  ```
// gap 만큼 떨어진 요소들을 삽입 정렬. 정렬의 범위는 first에서 last
inc_insertion_sort(int list[], int first, int last, int gap) {
	int i, j, key;
	for(i=first+gap ; i<=last ; i=i+gap){
		key = list[i];
		for(j=i-gap ; j>=first && key<list[ j] ; j=j-gap)
			list[j+gap]=list[ j];
		list[j+gap]=key;
	}
}
//                                           
void shell_sort( int list[], int n ) {
	int i, gap;
	for( gap=n/2 ; gap>0 ; gap = gap/2 ) {
		for(i=0 ; i<gap ; i++) // 부분 리스트의 개수는 gap
			inc_insertion_sort(list, i, n-1, gap);
    }
}
 ```
* 셸 정렬의 복잡도 분석
  * 셸정렬의 장점
    * 보다 적은 위치교환으로 제자리 찾을 가능성 증가
  * 시간적 복잡도
    * 셀 정렬의 성능은 간격에 따라 달라진다. 일반적으로 원소 개수의 ½를 사용하고 한 단계 수행될 때 마다 간격을 반으로 감소하면서 반복 수행
    * 최악의 경우 O(n2)
    * 평균적인 경우는 Gap의 크기에 따라 달라지며 수학적으로 분석하기 어려움
    * 실험적으로 평균적으로 O(n1.5)의 복잡도
    * 삽입 정렬(insertion sort)보다 개선된 정렬 방법 
                        
<br>

### 버블 정렬(Bubble Sort)
* 인접한 2개의 레코드를 비교하여 순서대로 되어 있지 않으면 서로 교환
* 이러한 비교-교환 과정을 리스트의 왼쪽 끝에서 오른쪽 끝까지 반복(스캔)
* 한번의 스캔이 완료되면 리스트의 오른쪽 끝에 가장 큰 레코드가 이동함
* 끝으로 이동한 레코드를 제외한 왼쪽 리스트에 대하여 스캔 과정 반복함
  ![](https://velog.velcdn.com/images/phwon7/post/47af5cca-843e-424d-b81b-8db2f5b62594/image.png)
* 버블 정렬 소스코드
  ```
#define SWAP(x, y, t) ( (t)=(x), (x)=(y), (y)=(t) )
void bubble_sort(int list[], int n){
	int i, j, temp;
	for( i=n-1; i>0 ; i-- ){ //마지막 원소부터 정렬됨
		for( j=0; j<i ; j++ ) // 앞뒤의 레코드를 비교한 후 교환
			if ( list[ j] > list[ j+1] )
				SWAP(list[ j], list[ j+1], temp);
	}
}
                        
* 버블 정렬 복잡도 분석
  * 비교 횟수(최상, 평균, 최악의 경우 모두 일정) : O(n2)
  * 이동 횟수
    * 역순으로 정렬된 경우(최악의 경우) : 이동 횟수 = 3 * 비교 횟수
    * 이미 정렬된 경우(최선의 경우) : 이동 횟수 = 0
    * 평균의 경우 : O(n2)
  * 레코드의 이동 과다
    * 이동연산은 비교연산 보다 더 많은 시간이 소요됨
                        
<br>

### 합병 정렬(Merge Sort)
* 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분리스트를 정렬
* 정렬된 두 개의 부분 리스트를 합하여 전체 리스트를 정렬함
* 분할 정복(divide and conquer) 방법 사용
* 문제를 보다 작은 2개의 문제로 분리하고 각 문제를 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략
* 분리된 문제가 아직도 해결하기 어렵다면(즉 충분히 작지 않다면) 분할정복방법을 다시 적용(재귀호출 이용)
  ![](https://velog.velcdn.com/images/phwon7/post/685e3ab0-4cee-4875-9d1d-df5e1e88783c/image.png)
* 합병정렬 과정
  ① 분할 단계 : 정렬할 전체 자료의 집합에 대해서 최소 원소의 부분집합이 될 때까지 분할작업을 반복하여 1개의 원소를 가진 부분집합 8개를 만든다
  ② 병합단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합한다. 8개의 부분집합이 1개로 병합될 때까지 반복한다
  ![](https://velog.velcdn.com/images/phwon7/post/359cd80d-89e7-4672-8063-82002115746f/image.png)
* 합병정렬 알고리즘
  1. 만약 정렬하고자 하는 구간의 크기가 2이상이면
  2. 배열의 중간 위치 계산
  3. 왼쪽 부분 배열 정렬 : merge_sort 함수 순환 호출
  4. 오른쪽 부분 배열을 정렬 : merge_sort 함수 순환 호출
  5. 정렬된 2개의 부분 배열을 통합하여 하나의 정렬된 배열 만듦
    ![](https://velog.velcdn.com/images/phwon7/post/aea84a29-9da7-4af0-9d14-78231ddf0c4c/image.png)
    ![](https://velog.velcdn.com/images/phwon7/post/e8fd17d1-a006-490a-b1fc-46637adfa010/image.png)

|![](https://velog.velcdn.com/images/phwon7/post/514ba424-fc27-4ca2-b140-72bb1bb25a4e/image.png)|![](https://velog.velcdn.com/images/phwon7/post/438e6d2c-b468-4bdc-b019-8e56cd30dc7c/image.png)|
  |--|--|
  
* 합병정렬 소스코드
  ```
void merge_sort(int list[], int left, int right) {
	int mid;
	if(left<right) {
		mid = (left+right)/2;
		merge_sort(list, left, mid);
		merge_sort(list, mid+1, right);
		merge(list, left, mid, right);
	}
}
// i는 정렬된 왼쪽리스트에 대한 인덱스
// j는 정렬된 오른쪽리스트에 대한 인덱스
// k는 정렬될 리스트에 대한 인덱스
void merge(int list[], int left, int mid, int right){
	int sorted[MAX_SIZE]; // 임시 공간 필요
	int i, j, k, l;
	i=left; j=mid+1; k=left;
	// 분할 정렬된 list의 합병
	while(i<=mid && j<=right){
		if(list[i]<=list[ j]) sorted[k++] = list[i++];
		else sorted[k++] = list[ j++];
	}
	if(i>mid) // 남아있는 오른쪽배열 일괄복사
		for(l=j; l<=right; l++)
			sorted[k++] = list[l];
	else // 남아있는 왼쪽배열 일괄복사
		for(l=i; l<=mid; l++)
			sorted[k++] = list[l];
	// 배열 sorted[]의 리스트를 배열 list[]로 복사
	for(l=left; l<=right; l++)
		list[l] = sorted[l];
}
  ```

* 합병정렬 복잡도 분석
  * 비교 횟수
    * 분할단계: 크기 n인 리스트를 정확히 균등 분할하므로 log(n)번의 순환 호출 필요, 비교나 이동은 일어나지 않음
    * 병합단계: 각 분할된 배열에서 리스트의 모든 레코드 n개를 비교하여 병합하기 때문에 한 단계의 분할을 병합하는데 최대 n번의 비교 연산
    * 따라서 전체 비교 복잡도는 n*log(n)
  * 이동 횟수
    * 레코드의 이동이 각 분할에서 2n번 발생하므로 전체 레코드의 이동은 2n*log(n)번 발생
    * 최적, 평균, 최악의 경우 큰 차이 없이 O(n*log(n))의 복잡도
    * 안정적이며 데이터의 초기 분산 순서에 영향을 덜 받음
    * 추가적인 메모리가 필요
