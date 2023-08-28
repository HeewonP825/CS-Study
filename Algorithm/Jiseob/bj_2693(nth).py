'''
풀이 방향:
map 함수로 정수 리스트 생성 -> sort로 정렬 -> 음수 인덱스 이용 출력
'''

T=int(input())
N=3
result=[]

while T:
    num_list=list(map(int,input().split()))
    num_list.sort()             # 주의: sort 함수는 정렬 후 None을 반환, 정렬된 리스트 반환하는 것 아님
    result.append(num_list[-N])
    T-=1

for i in result:
    print(i)
