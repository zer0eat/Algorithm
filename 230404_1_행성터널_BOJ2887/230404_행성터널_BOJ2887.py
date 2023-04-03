# 행성터널_BOJ12887

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                            # 행성의 개수

lst = []                                    # 행성의 정보를 저장할 리스트 생성
for k in range(N):                          # 행성의 개수를 반복해서
    x, y, z = map(int, input().split())     # 행성의 x, y, z 좌표를 input 받고
    lst.append([x, y, z, k])                # lst에 [x, y, z, k(행성의번호)]를 append 한다

x_star = lst[:]                             # lst를 x_star에 깊은 복사한 후
x_star.sort(key=lambda i : i[0])            # 0번 인덱스로 오름차순 정렬한다
y_star = lst[:]                             # lst를 y_star에 깊은 복사한 후
y_star.sort(key=lambda i : i[1])            # 1번 인덱스로 오름차순 정렬한다
z_star = lst[:]                             # lst를 z_star에 깊은 복사한 후
z_star.sort(key=lambda i : i[2])            # 2번 인덱스로 오름차순 정렬한다

star = dict()                               # 별을 연결할 비용을 저장할 딕셔너리를 생성하고
for i in range(1, N):                       # 1부터 N-1까지 반복한다
    length_x = min(abs(x_star[i][0]-x_star[i-1][0]), abs(x_star[i][1]-x_star[i-1][1]), abs(x_star[i][2]-x_star[i-1][2]))    # 0번 인덱스 정렬시 i-1번 별과 i번 별 사이의 거리를 저장한다
    length_y = min(abs(y_star[i][0]-y_star[i-1][0]), abs(y_star[i][1]-y_star[i-1][1]), abs(y_star[i][2]-y_star[i-1][2]))    # 1번 인덱스 정렬시 i-1번 별과 i번 별 사이의 거리를 저장한다
    length_z = min(abs(z_star[i][0]-z_star[i-1][0]), abs(z_star[i][1]-z_star[i-1][1]), abs(z_star[i][2]-z_star[i-1][2]))    # 2번 인덱스 정렬시 i-1번 별과 i번 별 사이의 거리를 저장한다

    if star.get(x_star[i][3]) == None:      # x_star 리스트에 i번째 별의 번호가 key인 원소가 없다면
        star[x_star[i][3]] = [[length_x, x_star[i-1][3]]]       # x_star 리스트에 i번째 별의 번호가 key인 원소를 생성하고 [[터널 비용, x_star 리스트에 i-1번째 별의 번호]]를 저장한다
    else:                                   # x_star 리스트에 i번째 별의 번호가 key인 원소가 있다면
        star[x_star[i][3]].append([length_x, x_star[i-1][3]])   # x_star 리스트에 i번째 별의 번호가 key인 원소에 [터널 비용, x_star 리스트에 i-1번째 별의 번호]를 append
    if star.get(x_star[i-1][3]) == None:    # x_star 리스트에 i-1번째 별의 번호가 key인 원소가 없다면
        star[x_star[i-1][3]] = [[length_x, x_star[i][3]]]       # x_star 리스트에 i-1번째 별의 번호가 key인 원소를 생성하고 [[터널 비용, x_star 리스트에 i번째 별의 번호]]를 저장한다
    else:                                   # x_star 리스트에 i-1번째 별의 번호가 key인 원소가 있다면
        star[x_star[i-1][3]].append([length_x, x_star[i][3]])   # x_star 리스트에 i-1번째 별의 번호가 key인 원소에 [터널 비용, x_star 리스트에 i번째 별의 번호]를 append

    if star.get(y_star[i][3]) == None:      # y_star 리스트에 i번째 별의 번호가 key인 원소가 없다면
        star[y_star[i][3]] = [[length_y, y_star[i-1][3]]]       # y_star 리스트에 i번째 별의 번호가 key인 원소를 생성하고 [[터널 비용, y_star 리스트에 i-1번째 별의 번호]]를 저장한다
    else:                                   # y_star 리스트에 i번째 별의 번호가 key인 원소가 있다면
        star[y_star[i][3]].append([length_y, y_star[i-1][3]])   # y_star 리스트에 i번째 별의 번호가 key인 원소에 [터널 비용, y_star 리스트에 i-1번째 별의 번호]를 append
    if star.get(y_star[i-1][3]) == None:    # y_star 리스트에 i-1번째 별의 번호가 key인 원소가 없다면
        star[y_star[i-1][3]] = [[length_y, y_star[i][3]]]       # y_star 리스트에 i-1번째 별의 번호가 key인 원소를 생성하고 [[터널 비용, y_star 리스트에 i번째 별의 번호]]를 저장한다
    else:                                   # y_star 리스트에 i-1번째 별의 번호가 key인 원소가 있다면
        star[y_star[i-1][3]].append([length_y, y_star[i][3]])   # y_star 리스트에 i-1번째 별의 번호가 key인 원소에 [터널 비용, y_star 리스트에 i번째 별의 번호]를 append

    if star.get(z_star[i][3]) == None:      # z_star 리스트에 i번째 별의 번호가 key인 원소가 없다면
        star[z_star[i][3]] = [[length_z, z_star[i-1][3]]]       # z_star 리스트에 i번째 별의 번호가 key인 원소를 생성하고 [[터널 비용, z_star 리스트에 i-1번째 별의 번호]]를 저장한다
    else:                                   # z_star 리스트에 i번째 별의 번호가 key인 원소가 있다면
        star[z_star[i][3]].append([length_z, z_star[i-1][3]])   # z_star 리스트에 i번째 별의 번호가 key인 원소에 [터널 비용, z_star 리스트에 i-1번째 별의 번호]를 append
    if star.get(z_star[i-1][3]) == None:    # z_star 리스트에 i-1번째 별의 번호가 key인 원소가 없다면
        star[z_star[i-1][3]] = [[length_z, z_star[i][3]]]       # z_star 리스트에 i-1번째 별의 번호가 key인 원소를 생성하고 [[터널 비용, z_star 리스트에 i번째 별의 번호]]를 저장한다
    else:                                   # z_star 리스트에 i-1번째 별의 번호가 key인 원소가 있다면
        star[z_star[i-1][3]].append([length_z, z_star[i][3]])   # z_star 리스트에 i-1번째 별의 번호가 key인 원소에 [터널 비용, z_star 리스트에 i번째 별의 번호]를 append

visited = [0] * N                           # 방문표시를할 리스트를 생성하고
ans = 0                                     # 별을 모두 연결했을 때 터널비용을 저장할 변수를 생성한다
tmp = [[0, 0]]                              # [비용, 시작별]을 tmp 리스트 안에 넣고 생성해서
while tmp:                                  # tmp가 빌때까지 반복한다
    A = heapq.heappop(tmp)                  # tmp에서 heappop해서 A에 저장한 후
    if visited[A[1]] == 0:                  # 만약 A[1]번 별에 방문 전이라면
        visited[A[1]] = 1                   # 방문 표시를 하고
        ans += A[0]                         # ans에 터널 비용을 더한다
        for i in star[A[1]]:                # A[1]번 별과 연결된 별을 반복해서
            if visited[i[1]] == 0:          # 해당 별이 방문 전이라면
                heapq.heappush(tmp, i)      # tmp에 heappush한다
print(ans)                                  # while문이 종료되었다면 터널의 공사비용을 출력한다