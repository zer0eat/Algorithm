# 분수찾기_BOJ1193

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())               # 찾으려는 분수의 순서
cnt = 0                                     # 분수의 순서를 저장하기 위한 변수
for a in range(10000000):                   # 10000000을 반복해서
    for b in range(a+1):                    # 대각선 a번 째 줄에 나올 수 있는 분수의 개수인 a+1개만큼 반복한다
        if a % 2 == 0:                      # a가 짝수인 줄은
            x = a - b                       # 분자가 a-b
            y = b                           # 분모가 b 가되고
            cnt += 1                        # 분수의 순서를 1 올려준다
            if cnt == N:                    # 분수의 순서가 찾으려는 순서에 도달하면
                print(f'{x+1}/{y+1}')       # 분모와 분자에 1 씩 더해서 출력해주고
                exit()                      # 종료한다
        elif a % 2 == 1:                    # a가 홀수인 줄은
            y = a - b                       # 분모가 a-b
            x = b                           # 분자가 b 가되고
            cnt += 1                        # 분수의 순서를 1 올려준다
            if cnt == N:                    # 분수의 순서가 찾으려는 순서에 도달하면
                print(f'{x+1}/{y+1}')       # 분모와 분자에 1 씩 더해서 출력해주고
                exit()                      # 종료한다
