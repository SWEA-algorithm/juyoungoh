T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    minV = 10000000
    maxV = 0
    for i in range(N):
        if data[i] < minV:
            minV = data[i]
        if data[i] > maxV:
            maxV = data[i]
    print(f'#{tc} {maxV - minV}')