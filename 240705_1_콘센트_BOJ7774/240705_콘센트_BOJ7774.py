# 콘센트_BOJ7774

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 첫번째 멀티탭의 개수 / M 두번째 멀티탭의 개수를 input 받고
c1 = list(map(int, input().split()))    # 첫번째 멀티탭의 콘센트 개수를 리스트로 input 받고
c2 = list(map(int, input().split()))    # 두번째 멀티탭의 콘센트 개수를 리스트로 input 받고
c1.sort()                               # 첫번째 멀티탭의 개수를 오름차순으로 정렬하고
c2.sort()                               # 두번째 멀티탭의 개수를 오름차순으로 정렬한다
concent = [1, 0]                        # A타입과 B타입의 콘센트 수를 저장할 리스트를 생성하고
ans = 1                                 # 정답을 저장할 변수를 생성한다
while c1 and c2:                        # 두 종류의 멀티탭 중 하나라도 다 쓸 때까지 반복해서
    if concent[1] > 0:                  # B를 사용하는 A 콘센트를 꽂을 곳이 있다면
        concent[1] -= 1                 # B 콘센트의 수를 1 빼고
        concent[0] += c2.pop()          # A 콘센트의 수를 추가한다
    elif concent[0] > 0:                # A를 사용하는 B 콘센트를 꽂을 곳이 있다면
        concent[0] -= 1                 # A 콘센트의 수를 1 빼고
        concent[1] += c1.pop()          # B 콘센트의 수를 추가한다
    ans = max(ans, concent[0])          # A 콘센트의 최대치를 ans에 저장한다
if concent[1] and c2:                   # B 콘센트의 구멍이 남고 c1 멀티탭이 남았다면
    for n in range(concent[1]):         # 남은 구멍만큼 반복해서
        if c2:                          # 꽂을 멀티탭이 있다면
            concent[0] += c2.pop()      # A 콘센트의 수를 추가한다
        else:                           # 꽂을 멀티탭이 없다면
            break                       # for문을 break한다
print(max(ans,concent[0]))              # 최대 몇 개의 컴퓨터를 사용할 수 있는지 출력한다