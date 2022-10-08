T = int(input())
for tc in range(1, T + 1):
    s1 = input()
    s2 = input()
    is_in = 0
    if s1 in s2:
        is_in = 1
    print(f'#{tc} {is_in}')