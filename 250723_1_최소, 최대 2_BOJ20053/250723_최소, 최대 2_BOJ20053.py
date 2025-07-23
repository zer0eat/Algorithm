# 최소, 최대 2_BOJ20053

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트케이스를 input받고
for t in range(T):                          # 테스트케이스를 반복해서
    N = int(input())                        # 숫자의 수를 input받고
    lst = list(map(int, input().split()))   # 숫자 리스트를 input받는다
    print(min(lst), max(lst))               # 최소, 최대 숫자를 출력한다