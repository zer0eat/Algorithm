# 다리놓기_BOJ1010

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                           # 테스트 케이스
for t in range(T):                                      # 테스트 케이스를 반복해서
    N, M = map(int, sys.stdin.readline().split())       # N 강 왼편의 설치장소의 수 / M 강 오른편의 설치장소의 수

    z = 1                                               # 경우의 수를 계산할 변수 생성
    ans = 1                                             # 설치 경우의 수를 저장할 변수 생성
    for n in range(N):                                  # C(N,M)의 조합을 구하기 위해 N번 반복해서
        ans *= M                                        # ans에 M을 곱하고
        M -= 1                                          # M에서 1을 빼준다
        ans //= z                                       # ans에서 z를 나누고
        z += 1                                          # z에 1을 더해준다
    else:                                               # 반복을 마치면
        print(ans)                                      # M부터 M-N+1까지 곱하고 1부터 N까지 나누어 조합을 구한 수를 출력한다
