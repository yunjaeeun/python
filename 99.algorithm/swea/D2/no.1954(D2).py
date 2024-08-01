T = int(input())
# 0  1  2  3
# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())  # 달팽이 크기

    snail = [[0] * N for _ in range(N)]
    # 방향 dr[0] = 우, dr[1] = 하
    d = 0
    # 현재 위치 (0, 0)에서 시작
    r, c = 0, 0

    for i in range(1, N * N + 1):
        # 방향을 언제 바꿔야 할까?
        if r > N - 1 or c > N - 1 or snail[r][c] != 0:
            if d == 3:
                r -= di[d]
                c -= dj[d]
                d = 0

            else:
                r -= di[d]
                c -= dj[d]
                d += 1
                r += di[d]
                c += dj[d]
                snail[r][c] = i
        else:
            snail[r][c] = i
            print(snail)
            r += di[d]
            c += dj[d]

    print(snail)

        # 배열의 범위를 벗어났을때
        # 내가 이전에 놓은 숫자를 만났을떄
