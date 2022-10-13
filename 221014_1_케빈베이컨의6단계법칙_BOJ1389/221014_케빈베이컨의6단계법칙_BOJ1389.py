# 케빈베이컨의6단계법칙_BOJ1389

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def kevin(V):                                           # 케빈베이컨수를 구할 함수
    visited = [0]*(N+1)                                 # 방문여부를 체크할 리스트 생성
    cnt = 0                                             # 케빈베이컨값의 합을 저장할 변수 생성
    q = [[V,0]]                                         # 시작 값을 q에 넣고 시작
    while q:                                            # q가 빌때까지 반복해서
        a = q.pop(0)                                    # q에서 맨앞의 요소를 pop한 후
        if visited[a[0]] == 0:                          # 방문하지 않았으면
            visited[a[0]] = 1                           # 방문표시를 하고
            cnt += a[1]                                 # 케빈베이컨 수를 cnt에 더한다
            for f in friends[a[0]]:                     # 해당 번호의 친구리스트를 돌면서
                q.append([f, a[1]+1])                   # q에 [친구번호, 케빈베이컨수]를 append 한다
    return cnt                                          # 반복이 끝났다면 cnt를 return

# input 받기
N, M = map(int, sys.stdin.readline().split())           # N 유저의 수 / M 친구관계의 수

friends = [[] for _ in range(N+1)]                      # 친구관계를 저장할 빈리스트를 만들고

for _ in range(M):                                      # 친구관계의 수만큼 반복해서
    a, b = map(int, sys.stdin.readline().split())       # 친구관계를 맺은 a,b를 각각 저장하고
    friends[a].append(b)                                # a를 인덱스로 b를 append 하고
    friends[b].append(a)                                # b를 인덱스로 a를 append 한다

mini = 500000                                           # 최소 케빈베이컨 값을 저장할 변수를 생성하고
ans = 0                                                 # 최소 번호를 저장할 변수를 생성한 후
for k in range(1, N+1):                                 # 1번 부터 N번까지 반복해서
    v = kevin(k)                                        # k번의 케빈베이컨 수를 v에 저장하고
    if v < mini:                                        # v가 mini 보다작다면
        mini = v                                        # mini를 v로 바꾸고
        ans = k                                         # ans에 최소번호를 저장한다

print(ans)                                              # 최소번호를 출력한다