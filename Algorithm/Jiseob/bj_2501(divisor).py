'''
풀이 방향: 
약수(N의 약수를 찾기 위해서는 N의 제곱근까지만 탐색하면 됨) 리스트 -> set 이용 같은 수 필터링 -> sort -> 인덱스 이용 출력
'''

from math import sqrt

N, K = map(int, input().split())    # map, input, split -> N, K 받음
divisors=[]                         # 약수 담을 리스트
for i in range(1,int(sqrt(N))+1):         # 처음에는 N/2까지 탐색 -> 조사해보니 sqrt(N)까지만 탐색하면 됨
    if N%i == 0:
        divisors.append(i)          
        divisors.append(N//i)       # i로 나눈 몫도 약수로 추가
divisors=list(set(divisors))        # set() 이용 중복 없애기
divisors.sort()                     
if len(divisors) < K:
    print("0")
else:
    print(f"{divisors[K-1]}")

'''
References:
1. https://doodle-ns.tistory.com/32 : 약수 구하기 알고리즘
'''
