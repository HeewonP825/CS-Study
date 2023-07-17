# 1.1 배열

## 배열이란?
+ 배열은 연속된 메모리 공간에 순차적으로 저장된 데이터 모음이다. **<index. value>**
 
+ 대부분에 프로그램 언어에서 동일 타입의 데이터를 저장한다.

  - ex) 예를 들어 배열이 "int"타입인 경우 int 요소만 저장할 수 있으며 double, float, char 등과 같은 다른 타입은 저장할 수 없다.
 
+ 배열을 구성하는 각각의 value를 **요소(element)**라고 하며, 배열에서의 위치를 가리키는 숫자는 **인덱스(index)**라고 한다.

<br>

## 배열의 특징
* 동일한 데이터 유형을 가진다.
    * 주로 동일한 데이터 유형을 가지지만 이질형 데이터도 지원 가능한 프로그래밍 언어(ex: C언어의 구조체)도 있다.
    * 이질형 데이터들이 모인 집합체는 주로 레코드라고 함.

* 배열의 각 요소에 접근하는 시간은 O(1)로 모두 동일하다.
    * 기본위치 + 오프셋(요소크기 * 인덱스) 연산으로 모든 요소에 접근 가능하다.
* 연속된 메모리에 단일 블록화하여 데이터를 저장한다.
    * 낭비되는 공간이 거의 없다.
    * 다만, 크기가 매우 큰 배열일 경우, 필요 메모리 할당이 불가능할 수도 있다.
* 실제 메모리 상에서 물리적으로 데이터가 순차적으로 저장되기 때문에 데이터에 index가 존재하여 indexing 및 slicing이 가능하다.
    * indexing : index를 사용해 특정 요소를 리스트로 부터 읽어들이는 것
    * slicing : 요소에 특정 부분을 따로 분리해 조작하는 것

<br>

## C에서의 배열
### * 1차원 배열(One-dimensional Arrays)
|int list[5]; <br> int *plist[5];|![](https://velog.velcdn.com/images/phwon7/post/b0c15b70-c622-48a1-a846-bcf3d319186d/image.png)|
|--|--|

<img width="339" alt="스크린샷 2023-07-17 오후 6 58 52" src="https://github.com/HeewonP825/CS-Study/assets/80496838/e4a64d85-4a31-4125-b705-fd5ef0b4b76c">


+ 연속된 메모리 공간에 데이터들이 순차적으로 저장되어 있다.
+ C에서 인덱스는 0부터 시작한다.
+ 배열 크기는 5이므로 5개의 value를 저장할 수 있다.
+ 각 요소는 인덱스를 통해 액세스 할 수 있다.
+ C에서의 배열 전달은 **pass by address** (배열 전체를 복사해서 전달하지 않음)

  + 호출 시 input(==&input[0])을 매개변수 list 로 복사
+ C에서 parameter passing은 **call-by-value** 이다. Pointer parameter도 주소 값만 전달받는다.
+ list의 값을 변경해도 input의 내용은 변하지 않는다. 그러나, **dereference operator(역참조 연산자 *)**를 이용하면 변경 가능하다.
  * _주소를 통해 그 값에 접근하는 것을 역참조(dereference)_
+ C에서 parameter passing은 call-by-value이지만
dereference operator를 이용하여 array 값 혹은 pointer parameter 내용을 바꿀 수 있다.

<br>

### * 동적할당 배열(Dynamically Allocated Arrays)
|![](https://velog.velcdn.com/images/phwon7/post/807b28fb-ce5e-4cb2-92ea-8be3668dea54/image.png)|![](https://velog.velcdn.com/images/phwon7/post/2854b274-cc12-42d9-96a9-eb5c754adf69/image.png) <br> ![](https://velog.velcdn.com/images/phwon7/post/eb91c1cb-1d77-4dbd-9d2f-120d0beee41e/image.png)|
|--|--|
* n<1이거나 정렬할 숫자 목록을 저장할 메모리가 부족한 경우에는 실행이 실패한다.

<br>

### * 다차원 배열(Multidimensional Arrays)
다차원 배열이란 2차원 이상의 배열을 의미하며, 배열 요소로 또 다른 배열을 가지는 배열을 의미한다.
+ ex) 2차원 배열: 배열 요소로 1차원 배열을 가지는 배열
	  3차원 배열: 배열 요소로 2차원 배열을 가지는 배열
      4차원 배열: 배열 요소로 3차원 배열을 가지는 배열
      
![](https://velog.velcdn.com/images/phwon7/post/bcd98aa4-4078-4647-911e-2fa585977004/image.png)

<br>

## 배열의 장단점
### 장점

* 인덱스를 이용한 접근이 가능하기 때문에 모든 value에 빠르게 접근할 수 있다.
* 리스트, 그래프 등은 데이터 외에 포인터 등 추가적인 공간이 필요하지만, 배열은 데이터만 저장하기 때문에 공간 낭비가 적다.
* 간단하고 사용하기 쉽다.
 
### 단점

* 배열을 선언 한 이후에는 할당 된 정적 메모리 때문에 크기를 변경할 수 없다.

  + heap을 이용하여 배열의 크기를 컴파일 단계가 아닌 실행시간에 가변적으로 바꿀 수 있는 동적 배열 제외
  
* 중간에 특정 요소를 삽입 및 삭제하는 경우, 항상 메모리가 순차적으로 이어져 있어야 하기 때문에 삽입 및 삭제된 요소부터 그 뒤에 있는 모든 요소들을 이동시켜주어야 한다. 그렇기 때문에 삽입 및 삭제에 비용이 많이 들게 된다.
* 정적 배열의 경우 삽입과 삭제가 동적으로 발생하는 상황에서 적절한 배열의 크기를 미리 결정하는 것이 어렵고, 이로 인해 오버플로우 혹은 저장공간의 낭비를 초래할 수 있다.

<br>

## 배열을 사용하는 경우

아래 상황에서 주로 배열을 사용합니다.

* 순차적인 데이터를 저장하며 값보다는 순서가 중요할 때
* 다차원 데이터를 다룰 때
* 어떤 특정 요소를 빠르게 읽어야 할 때
* 데이터 사이즈가 자주 바뀌지 않으며 요소가 자주 추가되거나 삭제되지 않을 때

<br>

# 1.2 구조체

## 구조체란?

**구조체(structures)**란 사용자가 기본 타입을 가지고 새롭게 정의할 수 있는 사용자 정의 타입이다. 

구조체는 기본 타입만으로는 나타낼 수 없는 복잡한 데이터를 표현할 수 있다.
**레코드(record)**라고도 부르며, data items의 모임이라고 할 수 있다. 
 
배열이 같은 타입의 변수 집합이라고 한다면, 구조체는 다양한 타입의 변수 집합을 하나의 타입으로 정의한 것 이다.

이때 구조체를 구성하는 변수를 구조체의 **멤버(member)** 또는 **멤버 변수(member variable)**라고 한다.

<br>

## 구조체의 사용

|구조체 선언|<img src="https://velog.velcdn.com/images/phwon7/post/118315b0-6ec2-4623-ad3c-03659e4eca7d/image.png" align="left"/>|
|--|--|
|**typedef 사용 시**|![](https://velog.velcdn.com/images/phwon7/post/7beae466-49fc-4f4c-967b-298000b10195/image.png)|
|**구조체 변수 초기화** <br> 멤버 연산자(.) 사용|![](https://velog.velcdn.com/images/phwon7/post/f4bf97c1-c5a9-4d24-a56b-07203e7a3c86/image.png) <br> **Person1 = {.name = “James”, .age = 10, .salary = 35000};** <br> 처럼 중괄호({}) 사용 가능|
|**구조체 안에 구조체**|<img src="https://velog.velcdn.com/images/phwon7/post/ce867a97-5811-4cda-9468-691373e6bd67/image.png"/>|

<br>

## 구조체의 사용 이유

+ 구조체는 **똑같은 변수를 여러번 사용해야 하는 경우**에 효과적으로 사용할 수 있다. 

    + 예를 들어, C언어를 이용해서 콘솔로 간단한 성적 시스템을 만든다고 가정할 때, 구조체를 사용하지 않는다면 여러명의 학생의 성적 변수를 일일이 계속해서 선언해주어야 할 것이다. 하지만 구조체를 사용하면** 여러개의 변수를 하나로 묶어서 관리할 수 있으므로 편리**하다.
    + 그룹화할 때 같은 자료형을 가진 변수들을 묶어 그룹화할 수 있고, 서로 다른 자료형을 가진 변수들을 묶어 그룹화할 수도 있다. 
+ C언어에서 구조체를 응용해서 할 수 있는 분야가 굉장히 많다. 
   + 함수에 인자값으로 구조체를 만들어 전달하는 방법
   + **구조체 안에 구조체를 만들어 서로 참조하게 만들어 사용**하게 하는 것도 가능하다.
 
<br>
<br>
<br>
<br>
<br>
     
### 포스팅 참조)
+ http://www.tcpschool.com/java/java_array_twoDimensional
+ https://yoongrammer.tistory.com/43
+ https://coding-factory.tistory.com/639

<br>
<br>

#### 원문: [https://velog.io/@phwon7/자료구조-배열-구조체](https://velog.io/@phwon7/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EB%B0%B0%EC%97%B4%EA%B3%BC-%EA%B5%AC%EC%A1%B0%EC%B2%B4)
