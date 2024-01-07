# 방 배정하기_BOJ14697

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C, N = map(int, input().split())          # A, B, C 방에 들어갈 수 있는 인원 / N 전체 학생 수를 input 받고
for a in range(N//A, -1, -1):                   # N명의 사람을 A방에 배정할 수 있는 최대 수부터 배정안하는 방법까지 반복해서
    if A*a == N:                                # N명을 A 방에 딱 맞게 배정했다면
        print(1)                                # 1을 출력하고
        quit()                                  # 종료한다
    for b in range((N-A*a)//B, -1, -1):         # N명의 사람을 B방에 배정할 수 있는 최대 수부터 배정안하는 방법까지 반복해서
        if A*a + B*b == N:                      # N명을 A, B 방에 딱 맞게 배정했다면
            print(1)                            # 1을 출력하고
            quit()                              # 종료한다
        for c in range((N-A*a-B*b)//C, -1, -1): # N명의 사람을 C방에 배정할 수 있는 최대 수부터 배정안하는 방법까지 반복해서
            if A*a + B*b + C*c == N:            # N명을 A, B, C 방에 딱 맞게 배정했다면
                print(1)                        # 1을 출력하고
                quit()                          # 종료한다
else:                                           # 모든 경우를 반복해도 방을 배정할 방법이 없다면
    print(0)                                    # 0을 출력한다