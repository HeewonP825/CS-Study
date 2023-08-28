'''
풀이 방향:
GCD: 두 수 중 작은 값 기준으로 약수 리스트 생성 -> 약수 리스트 최댓값 == GCD 
-> 서로소 관계라면 LCM = A*B, 아니라면 LCM = (A/(GCD) * B/(GCD) * GCD) == A*B/(GCD)
'''

GCD, LCM = 0, 0
divisor_list=[]
A, B = input().split()
A, B= int(A), int(B)

# GCD(최대공약수 계산)
for i in range(1, min(A,B)+1):
    if (A%i==0) & (B%i==0):
        divisor_list.append(i)
GCD=max(divisor_list)
print(GCD)

# LCM(최소공배수 계산) - GCD 이용
if GCD == 1:   # 서로소
    print(A*B)
else:
    print(int((A*B)/ (GCD)))