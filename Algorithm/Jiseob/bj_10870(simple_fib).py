'''
풀이 방향:
1. input의 크기가 20이하의 자연수로 주어졌으므로 재귀함수로 구현 -> fib
2. fib() 함수는 이전 값을 저장하지 않으므로, N이 커지면 시간이 기하급수적으로 상승
-> 이전 fib() 값을 저장하는 리스트 이용하여 faster_fib() 구현
'''

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
N=int(input())
print(fib(N))

fib_list=[0,1]

def faster_fib(n):
    if n < len(fib_list):
        return fib_list[n]
    elif n == len(fib_list):
        fib_list.append(fib_list[-2] + fib_list[-1])
        return fib_list[n]
    else:
        for j in range(len(fib_list), n+1):
            faster_fib(j)
N=int(input())
faster_fib(N)
print(fib_list[N])
