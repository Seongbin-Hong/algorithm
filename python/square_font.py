# 조건
# - 적용 가능한 가장 큰 글자의 크기를 구하고자 함
# - 글꼴은 정사각형
# - 크기는 1M 단위 이며 정수 1로 표현
# - 될 수 있는 한 최대로 font size 설정
# - Text 가로 배치
# - 단어 순서 변경 불가
# - 연속한 단어 사이에는 공백 필요 (공백도 하나의 글자로 취급)
# - 개행 시 공백을 둘 필요 없음
# - 각 단어는 하나의 줄에서 시작하고 끝맺어야 함
# - 만약 font size가 1 이어도 만족할 수 없다면, 0 출력
# - 두 번째 줄의 총 글자 수가 1000자가 넘지 않도록 예외 처리를 해야 함

# 순서
# 1. Test case 숫자 입력
# 2. H, W, N 입력
# .
# .
# .
# 9. Test case 입력 값 만큼 반복

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    H, W, N = map(int, input().split())
    words = [_ for _ in map(str, input().split())]
    w_len = [len(_) for _ in words]
    w_max = H
    if w_max > W:
        w_max = W

    max_font_size = 0
    for font_size in range(1, w_max+1):
        line_num = 1
        i_word = 0
        possible = False
        while line_num * font_size <= H:
            line_first = True
            current_len = 0
            while True:
                if line_first:
                    if font_size * (current_len + w_len[i_word]) <= W:
                        current_len += w_len[i_word]
                        i_word += 1
                        line_first = False
                        if i_word == len(w_len):
                            possible = True
                            break
                    else:
                        line_num += 1
                        break
                else:
                    if font_size * (current_len + w_len[i_word] + 1) <= W:
                        current_len += w_len[i_word] + 1
                        i_word += 1
                        if i_word == len(w_len):
                            possible = True
                            break
                    else:
                        line_num += 1
                        break
            if i_word == len(w_len):
                possible = True
                break

        if not possible:
            break
        else:
            max_font_size = font_size

    print("#%d" % test_case, int(max_font_size))
