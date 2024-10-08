# Can you add this_BOJ7891

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    x, y = map(int, input().split())    # 두 수를 input 받고
    print(x+y)                          # 두 수의 합을 출력한다