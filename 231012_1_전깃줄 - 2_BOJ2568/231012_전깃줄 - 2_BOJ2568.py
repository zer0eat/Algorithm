# 전깃줄 - 2_BOJ2568

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import bisect

# input 받기
N = int(input())                                        # 전깃줄의 개수를 input 받고
wire = []                                               # 전깃줄의 정보를 저장할 리스트를 생성한다
for i in range(N):                                      # 전깃줄의 개수를 반복해서
    wire.append(list(map(int, input().split())))        # 연결된 전봇대 A와 B정보를 input받아 wire에 append한다
wire.sort()                                             # wire에 저장된 정보를 전봇대 A 기준으로 오름차순 정렬하고
ans = [wire[0][1]]                                      # A 전봇대 맨앞과 연결된 B 정보를 넣은 리스트를 생성하고
cnt = [1]                                               # 순서를 넣은 리스트를 생성한다
for i in range(1, N):                                   # 1부터 N-1까지 반복해서
    if ans[-1] < wire[i][1]:                            # ans의 맨 뒤에 저장된 B의 위치보다 n번째 B의 위치가 더 크다면
        ans.append(wire[i][1])                          # ans에 n번째 B의 위치를 append하고
        cnt.append(len(ans))                            # 새로 들어온 정보의 순서를 ans의 길이로 append한다
    else:                                               # ans의 맨 뒤에 저장된 B의 위치보다 n번째 B의 위치가 더 작다면
        idx = bisect.bisect_left(ans, wire[i][1])       # n번째 B보다 처음으로 같거나 큰 원소를 ans에서 찾아 idx에 인덱스를 저장한 후
        ans[idx] = wire[i][1]                           # 해당 원소를 n번째 B의 위치로 저장하고
        cnt.append(idx+1)                               # i번째 정보의 순서를 idx+1로 append한다
print(N-len(ans))                                       # 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력하고
ans_num = len(ans)                                      # 교차하지 않는 전깃줄의 수를 저장한 변수를 생성하고
cut_wire = []                                           # 교차하지 않도록 없애야하는 전깃줄 정보를 저장할 리스트를 생성한다
for i in range(N-1,-1,-1):                              # 전깃줄의 정보를 뒤에서 앞으로 반복해서
    if cnt[i] == ans_num:                               # i번째 전깃줄 순서가 ans_num이면 자르지 않아도 되드는 전깃줄이므로
        ans_num -= 1                                    # ans_num에서 1을 뺀다
    else:                                               # i번째 전깃줄 순서가 ans_num이 아니면 잘라야하는 전깃줄이므로
        cut_wire.append(wire[i][0])                     # cut_wire 리스트에 해당 전깃줄의 A정보를 append한다
for n in range(len(cut_wire)-1,-1,-1):                  # 잘라야하는 cut_wire 리스트를 반대로 반복해서
    print(cut_wire[n])                                  # 잘라야하는 A 전깃줄의 번호를 출력한다