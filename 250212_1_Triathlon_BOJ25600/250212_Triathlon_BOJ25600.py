# Triathlon_BOJ25600

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 참가자의 수를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성하고
for n in range(N):                      # 참가자의 수를 반복해서
    a, d, g = map(int, input().split()) # 3가지 정답 수를 input 받고
    tmp = a * (d+g)                     # 점수를 구해서
    if a == (d+g):                      # 애드혹과 dp + 그리디가 같으면
        tmp *= 2                        # 점수를 2배를 한다
    ans = max(ans, tmp)                 # 최고점수를 저장하고
print(ans)                              # 참가자 중 최고점을 출력한다