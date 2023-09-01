'''
풀이 방향:
서로 다른 많은 수를 가능한 많이 더해야 -> 1부터 차례로 더하는 것 유추 
-> N*(N+1)/2 <= S, (N+1)*(N+2)/2 > S -> 최댓값 N 계산 가능
P: S == 1이면 조건을 만족하는 N이 없음 -> 위의 식은 N >= 2 대해서 성립, S == 1 -> return 1(예외 처리)
'''

S= int(input())

def find_N(sum):
    if sum == 1:
        return 1
    for N in range(sum):
        if (N*(N+1)/2 <= sum) and ((N+1)*(N+2)/2 > sum):
            return N
        
print(find_N(S))