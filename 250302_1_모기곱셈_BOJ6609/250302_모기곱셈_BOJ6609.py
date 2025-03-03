# 모기곱셈_BOJ6609

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                    # break가 나올 때까지 반복해서
    try:                    # input이 있다면
        M, P, L, E, R, S, N = map(int, input().split()) # 모기의 생애를 input 받고
        ans = M             # 정답을 모기의 수로 저장하고
        for n in range(N):  # N번의 주를 반복해서
            M = P//S        # 모기의 수를 구하고
            P = L//R        # 번데이기의 수를 구하고
            L = ans*E       # 알의 추를 구해서
            ans = M         # 모기의 수를 저장한다
        print(ans)          # N주 후 모기의 수를 출력한다
    except:                 # input이 없다면
        break               # while문을 break한다