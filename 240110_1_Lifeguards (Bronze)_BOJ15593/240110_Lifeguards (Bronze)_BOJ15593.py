# Lifeguards (Bronze)_BOJ15593

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 라이프 가드의 수를 input 받고
visited = [list(map(int, input().split())) for _ in range(N)]   # 라이프 가드의 근무시간을 input 받는다
ans = 0                                                         # 한명을 잘랐을 때 최대 근무시간을 저장할 변수를 생성하고
for i in range(N):                                              # 라이프가드의 수를 반복하고
    tmp = set()                                                 # 근무시간을 저장할 set을 생성한 후
    for j in range(N):                                          # 라이프가드의 수를 반복한다
        if i != j:                                              # i번째 라이프 가드가 아니라면
            for k in range(visited[j][0], visited[j][1]):       # 근무시간을 반복해서
                tmp.add(k)                                      # set에 add한다
    else:                                                       # i번째 라이프 가드 외 모든 근무 시간을 더했다면
        ans = max(ans, len(tmp))                                # ans에 현재 최대 시간과 tmp 중 더 긴 시간을 저장하고
print(ans)                                                      # 가장 긴 근무시간을 출력한다