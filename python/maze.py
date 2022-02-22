LOAD = 0
WALL = 1
ENTRANCE = 2
OUTLET = 3
FOOT_PRINT = 4

MOVE_WAYS: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

MAZE: list[list] = [
    [0, 2, 1, 1, 0],
    [1, 0, 1, 0, 3],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
]


def iswall(matrix: list[list], x: int, y: int) -> bool:
    if x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix):
        return True
    elif matrix[y][x] == WALL:
        return True

    return False


stack = list[tuple[int, int]]()
x, y = (0, 0)
result = 0  # 0 = fail or 1 = success

# Entrance 찾기
for index in range(len(MAZE)):
    if ENTRANCE in MAZE[index]:
        x = MAZE[index].index(2)
        y = index
        break

# Stack에 시작 위치 삽입
stack.append((x, y))

# Stack이 empty array가 될 때까지 반복
while stack:
    x, y = stack.pop()

    # 지나간 point는 4로 변경
    MAZE[y][x] = FOOT_PRINT
    for row in MAZE:
        print(row)
    print("\n")

    # 이동할 방향 검사 (4ways)
    for x2, y2 in MOVE_WAYS:
        dx = x + x2
        dy = y + y2

        if iswall(MAZE, dx, dy):
            continue

        if MAZE[dy][dx] == OUTLET:
            result = 1
            break
        elif MAZE[dy][dx] == LOAD:
            stack.append((dx, dy))

print(result)
