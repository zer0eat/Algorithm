# Contest Timing_BOJ5928

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                                 # 정답을 저장할 변수를 생성하고
D, H, M = map(int, input().split())     # 날짜, 시간, 분을 input 받고
if D < 11 or (D == 11 and H < 11) or (D == 11 and H == 11 and M < 11):  # 시작 시간 전이라면
    print(-1)                           # -1을 출력하고
else:                                   # 시작 시간 후라면
    ans += (M-11)                       # 분을 계산하고
    ans += (H-11)*60                    # 시간을 분으로 계산하고
    ans += (D-11)*60*24                 # 일을 분으로 계산해서
    print(ans)                          # 정답을 출력한다