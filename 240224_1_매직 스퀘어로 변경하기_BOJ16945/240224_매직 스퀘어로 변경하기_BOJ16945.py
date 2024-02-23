# 매직 스퀘어로 변경하기_BOJ16945

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = []                                          # 배열을 받을 리스트를 생성하고
for _ in range(3):                              # 3행의 배열을 반복해서
    A += list(map(int, input().split()))        # input 받은 행을 A리스트에 더해준다
visited = [0]*10                                # 방문표시를 할 리스트를 생성하고
ans = 1e9                                       # 정답을 저장할 변수를 생성한다

def recur(dep, magic):
    global ans                                  # ans를 global로 선언하고
    if dep == 3:                                # 깊이가 3이라면
        if sum(magic) != 15:                    # 첫번째 행의 합이 15가 아니라면
            return                              # return한다
    if dep == 6:                                # 깊이가 6이라면
        if sum(magic[3:]) != 15:                # 두번째 행의 합이 15가 아니라면
            return                              # return 한다
    if dep == 9:                                # 깊이가 9라면
        if sum(magic[6:]) != 15:                # 세번째 행의 합이 15가 아니라면
            return                              # return 한다
        if magic[0]+magic[3]+magic[6] != 15:    # 첫번째 열의 합이 15가 아니라면
            return                              # return 한다
        if magic[1]+magic[4]+magic[7] != 15:    # 두번째 열의 합이 15가 아니라면
            return                              # return 한다
        if magic[2]+magic[5]+magic[8] != 15:    # 세번째 열의 합이 15가 아니라면
            return                              # return 한다
        if magic[0]+magic[4]+magic[8] != 15:    # 오른쪽 아래로 내려가는 대각선의 합이 15가 아니라면
            return                              # return 한다
        if magic[2] + magic[4] + magic[6] != 15:# 왼쪽 아래로 내려가는 대각선의 합이 15가 아니라면
            return                              # return 한다
        tmp = 0                                 # 변경 비용을 저장할 변수를 생성하고
        for a in range(9):                      # 원소를 반복해서
            tmp += abs(A[a]-magic[a])           # 변경 비용을 tmp에 더해준다
        else:                                   # 모든 원소를 변경했다면
            ans = min(ans, tmp)                 # 정답과 tmp 중 더 작은 값을 저장한다
        return                                  # return 한다
    for i in range(1, 10):                      # 1부터 9까지 원소를 반복해서
        if visited[i]:                          # i가 이미 담겨 있다면
            continue                            # continue로 넘어간다
        visited[i] = True                       # i를 방문 표시하고
        magic.append(i)                         # i를 리스트에 담고
        recur(dep+1, magic)                     # 깊이 dep+1부터 매직스퀘어를 탐색한다
        magic.pop()                             # i를 리스트에서 pop하고
        visited[i] = False                      # i의 방문 표시를 해제한다

recur(0, [])                                    # 깊이 0부터 매직스퀘어를 탐색한다
print(ans)                                      # 배열 A를 매직 스퀘어로 변경하는 비용의 최솟값을 출력한다