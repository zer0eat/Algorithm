# 와우산 스탬프 투어_BOJ34543

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 명소의 개수를 input 받고
W = int(input())        # 총 걸음수를 input받고
ans = 0                 # 정답을 저장할 변수를 생성하고
ans += N*10             # 명소 개수만큼 점수를 더해주고
if N >= 3:              # 명소가 3개 이상이면
    ans += 20           # 추가 점수를 더해주고
if N == 5:              # 명소가 5개면
    ans += 50           # 추가 점수를 더해주고
if W > 1000:            # 걸음수가 1000보다 크면
    ans -= 15           # 점수를 깎아주고
if ans < 0:             # 점수가 음수면
    ans = 0             # 0으로 만들어준다
print(ans)              # 정답 출력한다