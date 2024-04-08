# 교수가 된 현우_BOJ3474

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())        # 테스트 케이스를 input 받고
for t in range(T):      # 테스트 케이스를 반복해서
    N = int(input())    # 정수 N을 input 받고
    cnt = 0             # 5의 개수를 셀 변수를 생성하고
    n = 5               # 5의 개수를 구할 변수를 생성한다
    while n <= N:       # N이 n보다 작아질때까지 반복해서
        cnt += N//n     # cnt에 N을 n으로 나눈 개수를 더해주고
        n *= 5          # n에 5를 곱해준다
    print(cnt)          # N! 뒤에 있는 0의 개수를 출력한다