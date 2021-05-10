# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1]) # a4 중 4 즉 row 는 숫자 받기.
column = int(ord(input_data[0])) - int(ord('a')) + 1 # a4 중 a a[0] 허나 a ~ h 까지 범위가 다양함 그걸 char 형태로 변경하여 컴퓨터에 입력하여야 함.ㄴ

#
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 앞서 dx,dy 를 이번에는 steps 로 대신하여 진행함.
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)