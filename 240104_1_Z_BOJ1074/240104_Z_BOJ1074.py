# Z_BOJ1074

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, R, C = map(int, input().split())     # N 배열 크기 / R 행의 위치 / C 열의 위치를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
while N > 0:                            # N이 0이 될때까지 반복해서
    N -= 1                              # 배열을 절반으로 줄이고
    # 2사분면
    if R < 2**N and C < 2**N:           # 4등분 했을 때 2사분면에 위치한다면
        pass                            # 패스한다
    # 1사분면
    elif R < 2**N and C >= 2**N:        # 4등분 했을 때 1사분면에 위치한다면
        ans += (2 ** N) * (2 ** N) * 1  # 2사분면을 모두 센 후 1사분면을 세게 되므로 ans에 해당 값을 추가하고
        C -= 2**N                       # 열의 위치를 전체의 절반만큼 빼준다
    # 3사분면
    elif R >= 2 ** N and C < 2 ** N:    # 4등분 했을 때 3사분면에 위치한다면
        ans += (2 ** N) * (2 ** N) * 2  # 2, 1사분면을 모두 센 후 3사분면을 세게 되므로 ans에 해당 값을 추가하고
        R -= 2**N                       # 행의 위치를 전체의 절반만큼 빼준다
    # 4사분면
    elif R >= 2 ** N and C >= 2 ** N:   # 4등분 했을 때 4사분면에 위치한다면
        ans += (2 ** N) * (2 ** N) * 3  # 2, 1, 3사분면을 모두 센 후 4사분면을 세게 되므로 ans에 해당 값을 추가하고
        R -= 2 ** N                     # 행의 위치를 전체의 절반만큼 빼준다
        C -= 2 ** N                     # 열의 위치를 전체의 절반만큼 빼준다
print(ans)                              # R, C를 방문하는 위치를 출력한다