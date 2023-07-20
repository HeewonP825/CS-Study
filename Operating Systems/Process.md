# 프로세스 내용 정리
## 프로그램 vs. 프로세스?
 A. 프로그램은 디스크에 저장된 실행파일, 프로세스는 실행중인 프로그램
 - 프로그램이 메모리에 올라가서 실행되면 프로세스가 됨

## 프로세스 주소 공간(Address Space)?
![IMG_1447](https://github.com/Jiseob-Byeon/CS-Study/assets/103080930/29e93344-4992-41d8-acfe-720b63a110b7)

**<C언어로 작성한 프로그램이 어떻게 메모리에 올라가는지 보여주는 그림>**
- 프로그램은 주소 공간을 번역(translate)하여 사용, 프로세스는 물리적 머신과 구분되는 주소 공간에서 실행
- 여러 요소로 구성(text, stack, data, heap)
- text: 프로그램 코드가 있는 영역 ex) for문
- stack: 일시적인 데이터(지역 변수, 함수 인자, 반환된 주소 등)를 저장하는 곳 ex) int *values, int i
- data: 전역 변수를 저장하는 곳 ex) int x, int y=15
- heap: 런타임(프로그램 실행 중)에 동적으로 할당된 메모리를 저장 (C언어를 예로 들면, malloc으로 할당한 주소가 저장) ex) values = (int*) malloc(sizeof(int)*5)

## 프로세스 상태
1. New: 프로그램이 생성됨
2. Running: 명령(Instruction)을 수행하고 있음
3. Waiting: 프로세스가 이벤트를 기다리고 있음
4. Ready: 프로세스가 프로세서에 할당되기를 기다리고 있음
5. Terminated: 프로세스가 실행을 종료

![IMG_1449](https://github.com/Jiseob-Byeon/CS-Study/assets/103080930/7739055a-8b93-4f71-a054-769e8a2d39fd)
**<프로세스는 실행하면서 상태가 변한다>**

## 프로세스 전환(Context Switch)
![IMG_1450](https://github.com/Jiseob-Byeon/CS-Study/assets/103080930/9c32055e-fad3-42e6-93e3-45e6e8f3d68f)

- Time multiplexing의 일종
- System Call, Interrupt, Trap(명령(Instruction) 수행 중 오류 발생) 발생 시 일어남
- CPU가 다른 프로세스로 전환되면, 기존 프로세스의 상태를 저장하고 저장된 새로운 프로세스의 상태를 가져와야 함
- Process Control Block(PCB, 각 프로세스의 정보를 저장)에 현재 상태(컨텍스트)를 저장. 새로운 상태도 PCB에서 읽어 옴.
- P: Context-Switch 시간은 overhead임( 시스템이 유용한 작업을 하지 않음 )

## fork, zombie, orphan
- fork(): 현재 프로세스의 복사본을 새로운 PID(Process IDentifier, 프로세스 식별, 관리에 사용)로 생성.
- 리눅스에서는 커널이 init 프로세스를 실행하고, 나머지 모든 프로세스는 init 의 자식 프로세스임.
- 리턴 값>0: 부모 프로세스, =0: 자녀 프로세스
- 부모 프로세스는 자녀 프로세스가 종료되는 것을 wait()으로 기다려줘야 함.(자원의 낭비를 막기 위해, 확인 필요)
- zombie(defunt): 부모 프로세스가 wait()을 호출하지 않고 자녀 프로세스가 종료
- orphan: 부모 프로세스가 자녀 프로세스보다 먼저 종료 
- 리눅스에서 OS가 orphan 프로세스를 init의 자식 프로세스로 바꿔줌

## Reference
1. 강순주 교수님 ppt 02, 03
2. https://www.kernelpanic.kr/16
