# 그룹나누기_14280

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def maketeam(a):
    if not team[a]:                                 # 팀을 구성할 팀원이 없다면
        return 0                                    # 0을 return
    c = team[a][:]                                  # c에다 같이 팀원을 할 리스트를 저장하고
    team[a] = []                                    # a의 리스트를 삭제한다
    visited[a-1] = 0                                # visited 팀을 구성했다고 0으로 표시한다
    for b in c:                                     # 팀원 리스트를 돌려서
        maketeam(b)                                 # 해당 팀원은 maketeam 함수를 돌린다
    return 1                                        # 팀원이 구성되었다면 1을 return

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    N, M = map(int, input().split())                # N 수업에 참여하는 사람의 수 / M 팀을 희망하는 순서쌍의 숫자
    arr = list(map(int, input().split()))           # 팀을 희망하는 순서쌍을 리스트로 받음

    team = [[] for _ in range(N+1)]                 # 팀을 연결할 빈 리스트를 생성하고
    visited = [1]*N                                 # 팀을 구성하지 않은 사람의 번호를 인덱스로 요소에 1을 표시한다

    for m in range(M):                              # 순서쌍만큼 반복해서
        a = arr[2 * m]                              # 팀을 구성하고 싶은 사람 중 하나를 a
        b = arr[2 * m + 1]                          # 다른 하나를 b에 저장하고
        team[a].append(b)                           # 한명을 인덱스로 다른 하나는 요소로 저장한다
        team[b].append(a)                           # 반대로 저장한다

    cnt = 0                                         # 팀을 셀 변수를 생성
    for a in range(1, N+1):                         # 1번부터 N번까지 반복해서
        cnt += maketeam(a)                          # 팀을 구성했다면 팀원과 함께 묶어 cnt에 1을 추가한다
    cnt += sum(visited)                             # 팀을 구성하지 않은 사람을 cnt에 모두 더한다
    print(f'#{t+1}',cnt)
