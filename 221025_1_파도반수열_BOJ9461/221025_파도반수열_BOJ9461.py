# 파도반수열_BOJ9461

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                   # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복해서
    N = int(sys.stdin.readline())               # 구하려는 삼각형의 번호

    P = [0, 1, 1, 1, 2]                         # 삼각형의 한변의 길이가 저장된 빈 리스트 생성
    if N > 4:                                   # N이 4보다 클때
        for n in range(4, N):                   # 4부터 N-1까지 반복해서
            P.append(P[n]+P[n-4])               # 11에 해당하는 한변의 길이인 P[n]+P[n-4]을 append
    print(P[N])                                 # N의 숫자를 출력한다