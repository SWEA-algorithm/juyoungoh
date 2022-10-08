# 10/8 11:57 - 12: 08
# 10 * 10 색칠하기 -> 10과 N을 헷갈리지 말자
# 왼쪽위, 오른쪽 아래 영역 -> 보라색 구하기
T = int(input())
for tc in range(1, T + 1):
    # N : 칠할 영역의 개수 
    N = int(input())
    board = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += color
                print(board[i][j], color)
    cnt = 0
    for r in range(10):
        for c in range(10):
            print(board[r][c], board[r][c] == 3)
            if board[r][c] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')