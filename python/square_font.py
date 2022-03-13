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

for tc in range(1, T + 1):
    H, W, N = map(int, input().split(" "))
    words = [word for word in map(str, input().split(" "))]
    words_len = [len(word) for word in words]

    # 정사각형 글꼴이기 때문에 높이를 신경써야 함
    max_digit = int()

    if H > W:
        max_digit = W
    else:
        max_digit = H  # H < W

    SPACE = 1
    max_font_size = 0

    for font_size in range(1, max_digit + 1):
        row_num = 1
        word_index = 0
        print_possible = False

        # W는 지속적으로 검증하기 때문에 H로 조건 생성
        while row_num * font_size <= H:
            first_time = True
            current_word_len = 0

            while True:
                first_current_square_size = font_size * \
                    (current_word_len + words_len[word_index])
                current_square_size = font_size * \
                    (current_word_len + SPACE + words_len[word_index])

                if first_time:
                    # W를 초과하지 않으면, 단어를 하나씩 추가함
                    if first_current_square_size <= W:
                        current_word_len += words_len[word_index]
                        word_index += 1
                        first_time = False
                        # index가 words_len을 초과하지 않게 조절함
                        if word_index == len(words_len):
                            print_possible = True
                            break
                    # W를 초과했으므로 다음 라인으로 넘어감
                    else:
                        row_num += 1
                        break

                else:
                    # 단어 + 단어가 되는 상황이므로 Space를 추가함
                    if current_square_size <= W:
                        current_word_len += SPACE + words_len[word_index]
                        word_index += 1
                        # index가 words_len을 초과하지 않게 조절함
                        if word_index == len(words_len):
                            print_possible = True
                            break
                    # W를 초과했으므로 다음 라인으로 넘어감
                    else:
                        row_num += 1
                        break
            # 처음부터 index가 words_len이 같은 경우를 위한 분기
            if word_index == len(words_len):
                print_possible = True
                break
        # 출력이 불가한 상태로, font size 0 출력
        if not print_possible:
            break
        else:
            max_font_size = font_size

    print(f"#{tc} {max_font_size}")
