'''
풀이 방향:
A, B를 각각 index(반복되는 숫자), offset(몇 번째)으로 나누자 -> index는 A에 0 이상의 정수를 빼는 식으로, 
                                                       offset은 자연수의 합 리스트를 이용하여 가장 가까우면서 작은 합의 index보다 1 크게
-> 합은 index가 같을 때 index), index가 1 차이날 때, index가 2 이상 차이날 때로 나누어 계산
사실 군수열 문제 -> index, offset으로 접근한 방법이 맞았음
'''

A,B=input().split()
A, B = int(A), int(B)
Atemp, Btemp = A, B
result=0
a_index=0
a_offset=0
b_index=0
b_offset=0  
sum_list=[int(0.5*i*(i+1)) for i in range(45)] # A, B는 최대 1000이므로 자연수의 합 리스트를 만들어 A, B와 비교


for i in range(46): # range(45)로 구하면 991부터 1000 사이의 숫자를 포함하지 못함 -> 에러 발생
    if A-i <= 0:
        a_index=i
        break
    else:
        a_index=i
        A -= i

for j in range(46):
    if B-j <= 0:
        b_index=j
        break
    else:
        B -= j
        b_index=j

a_offset = Atemp - sum_list[a_index-1]
b_offset = Btemp - sum_list[b_index-1]

if a_index == b_index:
    result = (b_offset - a_offset + 1) * a_index
elif b_index - a_index == 1:
    result = b_offset * b_index + (a_index- a_offset + 1) * a_index
else:
    temp_list=[k**2 for k in range(a_index+1, b_index)]
    result = b_offset * b_index + (a_index- a_offset + 1) * a_index + sum(temp_list)

print(f"{result}")