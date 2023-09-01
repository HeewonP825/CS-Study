'''
풀이 방향:
소수 구하기(2 ~ sqrt(num)+1 탐색 -> 소수 판정) -> flag 이용해서 for문 탈출한 것 표시
(이때 1은 소수가 아니므로 flag = 0으로 변환)
-> 소수 리스트에 추가 -> sum, min 구함
특이사항: O(N**(3/2))이므로 N = 10000까지도 시간 제한 만족
N = 1000000(백만) 이상이면 다른 알고리즘으로 구현해야
'''

from math import sqrt

prime_list=[]
M = int(input())
N = int(input())

for num in range(M, N+1):
    flag = 1
    if num == 1:                            # 1은 소수 아님
        flag = 0
    for i in range(2, int(sqrt(num))+1):   
        if num % i == 0:
            flag = 0
            break
    if flag == 1:
        prime_list.append(num)
if len(prime_list) != 0:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)