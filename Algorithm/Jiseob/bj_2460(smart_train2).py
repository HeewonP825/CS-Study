'''
풀이 방향:
처음에는 2개의 요소를 가지는 튜플 쌍으로 접근 -> max 구하기 어려움 -> 내리는/타는 사람 리스트, 전체 승객 리스트
-> 전체 승객 리스트에 내리는/타는 사람 수 반영되도록 
'''
get_on_off = []
passenger_num = [0]

for i in range(10):
    get_on_off.extend(list(map(int, input().split())))

for idx, num in enumerate(get_on_off):                  # range(len) 대신 enumerate 사용
    if idx % 2 == 0:
        passenger_num.append(passenger_num[-1]-num)
    else:
        passenger_num.append(passenger_num[-1]+num)
passenger_num = passenger_num[1:len(passenger_num)-1]   # 처음에 넣었던 0 제거, 마지막에 내리는 사람 0이니 제거
print(max(passenger_num))

'''
풀이 추가(가장 많은 사람 있었던 역 찾기)
max_index = passenger_num.index(max(passenger_num))
max_station = (max_index // 2) + 1
print(max_station)
'''