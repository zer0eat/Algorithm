# 팔찌 만들기_BOJ25707

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 구슬의 수를 input받고
beads = list(map(int, input().split())) # 구슬의 크기를 리스트로 input받는다
beads.sort()                            # 구슬의 크기를 오름차순으로 정렬하고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for n in range(N):                      # 구슬의 수를 반복해서
    ans += abs(beads[n-1] - beads[n])   # 구슬 크기 차의 절대값을 저장해서
print(ans)                              # 총합을 출력한다