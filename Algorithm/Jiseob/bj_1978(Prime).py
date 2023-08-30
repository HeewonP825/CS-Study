'''
풀이 방향:
약수 찾는 알고리즘(sqrt(N)까지 탐색) -> 1 제외 약수 없으면 True(소수)), 있으면 False 리턴
-> filter 함수 이용, True 반환하는 input 개수 count
'''

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
    return True

N = int(input())
num_list = list(map(int, input().split()))
print(len(list(filter(is_prime, num_list))))