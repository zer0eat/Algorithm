# 두~~부 두부 두부_BOJ25175

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, K = map(int, input().split()) # 참여인원수와 현재순서 부른 숫자를 input받고
while K < 0:                        # 부른숫자가 음수라면
    K += N                          # 참여인원수만큼 더해줘서
ans = (((K-3)%N)+M)                 # 다음 순서를 계산해서
if ans > N:                         # 해당 숫자가 참여인원수를 넘었다면
    ans %= N                        # 참여인원수 내 숫자로 바꿔주고
print(ans)                          # 다음차례의 순서를 출력한다