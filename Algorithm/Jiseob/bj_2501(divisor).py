N, K = map(int, input().split())    # map, input, split -> N, K 받음
divisors=[]                         # 약수 담을 리스트
for i in range(1,(N//2)+1):         
    if N%i == 0:
        divisors.append(i)          
        divisors.append(N//i)       # i로 나눈 몫도 약수로 추가
divisors=list(set(divisors))        # set() 이용 중복 없애기
divisors.sort()                     
if len(divisors) < K:
    print("0")
else:
    print(f"{divisors[K-1]}")