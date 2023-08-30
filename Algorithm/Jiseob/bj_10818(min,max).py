'''
풀이 방향:
list(map(int, input().split())) 이용 숫자 리스트 생성 -> max, min 함수로 최대, 최소 판정
'''

N=int(input()) # 최소, 최대 계산에는 필요없지만 없으면 두 번째 줄(숫자들) input 못 받음
num_list=list(map(int, input().split()))

print(f"{min(num_list)} {max(num_list)}")