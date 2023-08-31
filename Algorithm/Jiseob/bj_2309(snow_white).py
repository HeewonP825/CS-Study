'''
풀이 방향:
합이 100인 것 활용 -> 9명의 키를 더하면 100보다 클 것(offset) -> 더해서 offset과 같아지는 두 수 제거 -> sort
'''

dwarf_height = []
for i in range(9):
    dwarf_height.append(int(input()))

def sort_dwarf(height_list):        # 처음에는 함수 없이 작성 -> 더해서 offset과 같아지는 쌍이 두 쌍 이상 발생할 수 있음(이중 for문 탈출 어려움)
    height_sum = sum(height_list)   # ->  함수를 정의해서 return하는 식으로 변형
    offset = height_sum - 100
    for num1 in height_list:
        for num2 in height_list:
            if (num1 != num2) and ((num1+num2) == offset):
                height_list.remove(num1)
                height_list.remove(num2)
                height_list.sort()
                return height_list
            
dwarf_height = sort_dwarf(dwarf_height)
for height in dwarf_height:         # 출력 형태 확인(리스트 형태 출력 아니었음)
    print(height)