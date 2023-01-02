# 정수삼각형_BOJ1932

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                                   # 삼각형의 크기
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # tri 리스트에 삼각형을 input 받음
cnt = 2                                                                 # cnt라는 변수를 2로 저장하여 생성

for n in range(1, N):                                                   # 1부터 N-1까지 반복해서
    for c in range(cnt):                                                # cnt만큼 반박하여
        if c == 0:                                                      # c가 0이라 삼각형의 한 줄의 시작인 경우에는
            tmp = tri[n][c] + tri[n-1][c]                               # tmp에 n행 c열의 요소와 n-1행 c열의 요소를 더한 후
            tri[n][c] = tmp                                             # n행 c열의 요소를 tmp로 바꿔준다
        elif c == cnt-1:                                                # c가 cnt-1이라 삼각형의 한 줄의 끝인 경우에는
            tmp = tri[n][c] + tri[n-1][c-1]                             # tmp에 n행 c열의 요소와 n-1행 c-1열의 요소를 더한 후
            tri[n][c] = tmp                                             # n행 c열의 요소를 tmp로 바꿔준다
        else:                                                           # c가 삼각형의 한 줄의 중간인 경우에는
            tmp1 = tri[n][c] + tri[n - 1][c]                            # tmp1에 n행 c열의 요소와 n-1행 c열의 요소를 더하고
            tmp2 = tri[n][c] + tri[n - 1][c-1]                          # tmp2에 n행 c열의 요소와 n-1행 c-1열의 요소를 더한 후
            if tmp1 > tmp2:                                             # tmp1이 더 크다면
                tri[n][c] = tmp1                                        # n행 c열의 요소를 tmp로 바꿔준다
            else:                                                       # tmp2가 같거나 크다면
                tri[n][c] = tmp2                                        # n행 c열의 요소를 tmp로 바꿔준다
    else:                                                               # cnt의 반복이 끝났다면
        cnt += 1                                                        # cnt를 1 증가시키고
else:                                                                   # 1부터 N-1까지 반복이 끝났다면
    print(max(tri[N-1]))                                                # 마지막 열에서 가장 큰 수를 출력한다