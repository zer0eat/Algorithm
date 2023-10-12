# 꼬인 전기줄_BOJ1365

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import bisect

# input 받기
N = int(input())                                    # 전봇대의 개수를 input 받고
wire = list(map(int, input().split()))              # 길 왼편의 전봇대가 길 오른편의 몇 번 전봇대와 연결되어 있는지 리스트로 input받고
ans = [wire[0]]                                     # 길 왼편의 전봇대 맨앞과 연결된 길 오른편 전봇대 정보를 넣은 리스트를 생성하고
for i in range(1, N):                               # 길 왼편의 1번 인덱스부터 끝까지 반복해서
    if ans[-1] < wire[i]:                           # ans의 맨 뒤에 저장된 오른편 전봇대 번호보다 i번째 전봇대와 연결된 전봇대 번호가 뒤에 있다면
        ans.append(wire[i])                         # ans에 i번째 전봇대와 연결된 길 오른편의 전봇대 번호를 append한다
    else:                                           # ans의 맨 뒤에 저장된 오른편 전봇대 번호보다 i번째 전봇대와 연결된 전봇대 번호가 앞에 있다면
        idx = bisect.bisect_left(ans, wire[i])      # i번째 전봇대와 연결된 전봇대 번호보다 처음으로 같거나 큰 원소를 ans에서 찾아 idx에 인덱스를 저장한 후
        ans[idx] = wire[i]                          # 해당 원소를 i번째 전봇대와 연결된 전봇대 번호로 바꿔준다
print(N-len(ans))                                   # 전선이 꼬이지 않으려면 잘라야하는 전선의 수를 출력한다