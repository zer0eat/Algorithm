# 회의실배정_BOJ1931

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())               # T 회의의 수

meeting = []                                # 회의의 시작과 끝 시간을 담을 리스트
for t in range(T):                          # 회의의 수만큼 반복해서
    meeting.append(list(map(int, sys.stdin.readline().split())))    # 시작시간과 끝시간이 담긴 리스트를 meeting에 append

meeting.sort(key = lambda x:(x[1],x[0]))    # meeting 시간을 끝나는 시간으로 오름차순 정렬하고 같다면 시작시간으로 오름차순으로 정렬한다

cnt = 0                                     # 회의할 수 있는 개수를 셀 변수를 생성하고
endtime = 0                                 # 회의가 끝나는 시간을 저장할 변수를 생성한다
for m in meeting:                           # 회의를 반복해서
    if m[0] >= endtime:                     # 시작시간이 이전 회의시간보다 같거나 이후라면
        endtime = m[1]                      # 회의 끝나는 시간을 다음 회의의 끝나는 시간으로 변경하고
        cnt += 1                            # 회의 개수에 추가한다

print(cnt)