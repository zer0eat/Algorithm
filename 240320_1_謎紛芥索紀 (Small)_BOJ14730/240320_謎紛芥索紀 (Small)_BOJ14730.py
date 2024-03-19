# 謎紛芥索紀 (Small)_BOJ14730

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 항의 개수를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for n in range(N):                      # N개의 항을 반복해서
    a, b = map(int, input().split())    # 계수와 차수를 input 받고
    ans += a*b                          # 미분 후 x에 1을 대입했을 때 항의 값을 ans에 더한다
print(ans)                              # f’(1)의 값을 첫째 줄에 출력한다