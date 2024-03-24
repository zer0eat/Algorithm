# 게임을 만든 동준이_BOJ2847

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 레벨의 단계를 input 받고
score = [int(input()) for _ in range(N)]    # 레벨별 점수를 리스트로 input 받는다
ans = 0                                     # 점수를 내릴 횟수를 저장할 변수를 생성하고
now = score[-1]                             # 마지막 단계의 점수를 변수로 저장한다
for n in range(N-2, -1, -1):                # 뒤에서 부터 앞으로 반복해서
    if now <= score[n]:                     # 현재 단계보다 앞 단계 점수가 같거나 높으면
        ans += abs(score[n]-now+1)          # ans에 현재 단계보다 1만큼 낮아지도록 점수를 내릴 횟수를 더해준다
        now = now-1                         # now에 현재단계보다 1 낮은 점수를 저장한다
    else:                                   # 현재 단계보다 앞 단계 점수가 낮다면
        now = score[n]                      # now에 앞 단계 점수를 저장한다
print(ans)                                  # 점수를 몇 번 감소시키면 되는지 출력한다