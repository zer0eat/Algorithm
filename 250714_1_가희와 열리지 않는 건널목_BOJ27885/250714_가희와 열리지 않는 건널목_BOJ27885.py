# 가희와 열리지 않는 건널목_BOJ27885

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
c, h = map(int, input().split())                    # 상행선과 하행선의 수를 input받고
ans = [1]*3600*24                                   # 정답을 저장할 리스트를 생성하고
for n in range(c+h):                                # 상행선과 하행선을 반복해서
    time = list(map(int, input().split(':')))       # 시간을 input받고
    for m in range(40):                             # 기차가 지나가는 시간을 반복해서
        ans[time[0]*3600+time[1]*60+time[2]+m] = 0  # 차단기가 내려가 있는 시간을 저장하고
print(sum(ans))                                     # 차단기가 올라간 시간을 출력한다