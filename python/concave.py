def iswall(x, y, len):
    if x > len-1 or y > len-1:
        return True
    return False


T: int = int(input())

STONE = "o"
SPACE = "."

MOVE_DIRECTIONS = [(1, 0), (0, 1), (-1, 1), (1, 1)]


for test_case in range(1, T + 1):
    N: int = int(input())

    concave_space: list[list[str]] = [list(input()) for x in range(N)]
    """[
        ['o', 'o', 'o', 'o', 'o'],
        ['.', '.', '.', '.', 'o'],
        ['.', '.', '.', 'o', '.'],
        ['.', '.', 'o', '.', '.'],
        ['.', 'o', '.', '.', '.'],
        ['o', '.', '.', '.', '.'],
    ]"""

    done: bool = False
    stone_len: int = 0

    for i in range(len(concave_space)):
        if done:
            break
        for j in range(len(concave_space[i])):
            if concave_space[i][j] == STONE:
                stone_len = 1
                for direction in MOVE_DIRECTIONS:
                    dx, dy = direction
                    x = j
                    y = i
                    while True:
                        if stone_len == 5:
                            done = True
                            break
                        if iswall(y+dy, x+dx, N):
                            stone_len = 1
                            break
                        if concave_space[y+dy][x+dx] == STONE:
                            stone_len += 1
                            x += dx
                            y += dy
                        elif concave_space[y+dy][x+dx] == SPACE:
                            stone_len = 1
                            break
                stone_len = 0

            elif concave_space[i][j] == SPACE:
                stone_len = 0

    if done:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")

"""
....o
...o.
..o..
.o...
o....
"""
"""
............o......
.oo................
...................
o...o.......o.....o
.............ooo...
....o..............
...................
.o........o........
....o..............
............o......
..o.....o..o.......
..........o........
..o......o..o.....o
..o..o..o...o......
.o..........o...oo.
..o........o...o.o.
............o...o..
..o................
...................
"""
