# 숫자 재배치_BOJ16943

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 두 정수 A, B를 input 받고
A = str(A)                          # A를 문자열로 바꾼 후
visited = [0]*len(A)                # 순열의 포함 여부를 저장할 리스트를 생성하고
num = []                            # 순서를 바꾼 순열을 저장할 리스트를 생성한다

def recur(dep, tmp):
    if dep == len(A):               # 순열이 완성되었다면
        if tmp[0] != '0':           # 시작이 0이 아닌경우에
            num.append(int(tmp))    # num에 순열을 append하고
        return                      # return한다
    for i in range(len(A)):         # A의 길이 만큼 반복해서
        if visited[i]:              # i번째 수가 포함되어 있다면
            continue                # continue로 넘어간다
        visited[i] = True           # i번째 인덱스를 방문표시하고
        tmp += A[i]                 # i번째 수를 tmp에 더해주고
        recur(dep+1, tmp)           # dep+1 깊이부터 순열 순서를 탐색하고
        tmp = tmp[:dep]             # i번째 수를 제거해주고
        visited[i] = False          # i번째 인덱스를 방문표시를 해제한다

recur(0, '')                        # 0 깊이부터 순열 순서를 탐색한다
ans = -1                            # 정답을 저장할 변수를 생성하고
for n in num:                       # 순열을 반복해서
    if n < B:                       # 순열이 B보다 작은 수라면
        ans = max(ans, n)           # ans와 n 중 더 큰 값을 저장한다
print(ans)                          # B보다 작은 C중 가장 큰 값을 출력한다