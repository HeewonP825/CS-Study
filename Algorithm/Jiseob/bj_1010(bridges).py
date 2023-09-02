'''
풀이 방향:
최소 N개의 다리가 지어지고, 남은 사이트들은 N+1자리에 배분하면 됨(중복 조합) 
-> 서로 다른 (N+1) 자리에 중복 허용, 순서 상관없이 (M-N)개 배치
'''

from functools import reduce

T=int(input())
result_list=[]
for i in range(T):
    N, M = list(map(int,input().split()))
    if N == M:                  # N==M -> 다리 다 놓는 경우 뿐(1가지)
        result_list.append(1)
    else:                       # 정리하면 mCn
        numerator = reduce(lambda x,y: x*y, range(1, M+1))
        denominator = reduce(lambda x,y: x*y, range(1, M-N+1)) * reduce(lambda x,y: x*y, range(1, N+1))
        result = int(numerator/denominator)
        result_list.append(result)

for rslt in result_list:
    print(rslt)