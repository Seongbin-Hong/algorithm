T: int = int(input())

for test_case in range(1, T+1):
    N: int = int(input())

    matrix: list[list[str]] = [list(input()) for x in range(N)]

    cooldinates: list[list[tuple]] = []

    for i, row in enumerate(matrix):
        temp: list[tuple] = []
        for j, item in enumerate(row):
            if item == "#":
                temp.append((j, i))
        if temp:
            cooldinates.append(temp)

    standard_width: int = 0
    height: int = 0
    is_square = True

    if cooldinates:
        standard_width = len(cooldinates[0])
        start_point = cooldinates[0][0]

    else:
        is_square = False

    if standard_width == len(cooldinates):
        for i, row in enumerate(cooldinates):
            if is_square:
                if standard_width != len(row):
                    is_square = False
                    break

                temp_x = 0
                for j, point in enumerate(row):
                    x, y = point
                    if i == 0 and j == 0:
                        height = y

                    if height != y:
                        is_square = False
                        break

                    if j == 0:
                        temp_x = x
                        continue
                    elif x - temp_x != 1:
                        is_square = False
                        break

                    temp_x += 1

            else:
                break

            height += 1
    else:
        is_square = False

    if is_square:
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")
"""T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N: int = int(input())
    matrix = []

    for n in range(N):
        input_row = input().split(" ")
        matrix.append(input_row)

    cooldinates: list[list[tuple]] = []

    for i, row in enumerate(matrix):
        temp: list[tuple] = []
        for j, item in enumerate(row):
            if item == "#":
                temp.append((j, i))
        if temp:
            cooldinates.append(temp)

    standard_width: int = 0
    height: int = 0

    if cooldinates:
        standard_width = len(cooldinates[0])
        start_point = cooldinates[0][0]

    is_square = True
    if standard_width == len(cooldinates):
        for i, row in enumerate(cooldinates):
            if is_square:
                if standard_width != len(row):
                    is_square = False
                    break

                temp_x = 0
                for j, point in enumerate(row):
                    x, y = point
                    if i == 0 and j == 0:
                        height = y

                    if height != y:
                        is_square = False
                        break

                    if j == 0:
                        temp_x = x
                        continue
                    elif x - temp_x != 1:
                        is_square = False
                        break

                    temp_x += 1

            else:
                break

            height += 1

    if is_square:
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")
    # ///////////////////////////////////////////////////////////////////////////////////"""
