'''
풀이 방향:
피타고라스 정리 -> 가장 긴 변의 길이(빗변)의 제곱과 나머지 두 변의 길이의 제곱의 합을 비교 
-> 모든 변의 길이의 제곱의 합을 구하고, 가장 긴 변의 길이의 제곱 * 2를 뺌으로써, 나머지 두 변을 구별할 필요가 없어짐
'''

total_list = []
for i in range(30000):
    side_len = list(map(int, input().split()))
    if 0 in side_len:
        break
    h = max(side_len)
    total_sum = sum([num**2 for num in side_len])
    if total_sum - 2 * (h**2) == 0:
        total_list.append("right")
    else:
        total_list.append("wrong")
for result in total_list:
    print(result)
