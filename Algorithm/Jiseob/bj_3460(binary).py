T=int(input())
N_list=[]
for i in range(T):
    N_list.append(int(input()))

for i in range(T):
    bin_list=[j for j in bin(N_list[i])] # 파이썬 내장함수 bin 사용
    bin_list.reverse()
    bin_list.pop() # .pop()은 리스트에 저장된 값을 반환하므로 .pop().pop()은 불가능
    bin_list.pop()
    
    index_list=list(filter(lambda x: bin_list[x] == '1', range(len(bin_list))))
    '''
      filter(function, iterable): iterable의 요소 중 function을 참이 되게 하는 요소 반환
      -> range(len(bin_list)): bin_list(이진수 리스트)의 길이의 range -> index와 동일
    '''
    for index in index_list:
        print(index, end=" ") # 마지막 " " 지우려 print("\b") -> 채점 시 이스케이프 문자로 인식 -> 오류

'''
references: 1. https://bill1224.tistory.com/228: index 반환하는 함수
            2. bin()함수
'''