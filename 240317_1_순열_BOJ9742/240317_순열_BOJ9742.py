# 순열_BOJ9742

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def recur(dep, tmp, N):
    global cnt, flag                            # cnt와 flag를 글로벌 변수로 선언하고
    if flag or cnt > 3628800:                   # flag가 True이거나 cnt가 최종에 도달한경우
        return                                  # return한다
    if dep == N:                                # dep가 N이 되었다면
        if cnt == int(B):                       # cnt가 B번째에 도달한 경우
            flag = True                         # flag를 True로 저장하고
            print(f'{A} {B} = {tmp}')           # B번째 순열을 출력한다
        cnt += 1                                # cnt를 1 추가하고
        return                                  # return한다
    for i in range(N):                          # 문자열을 반복해서
        if visited[i]:                          # 방문했다면
            continue                            # continue로 넘어간다
        visited[i] = 1                          # i번째 원소를 방문표시하고
        recur(dep+1, tmp+lst[i], N)             # dep+1부터 B번째 순열을 탐색한다
        visited[i] = 0                          # i번째 원소를 방문표시 해제한다

while 1:                                        # break가 나올 때까지 반복해서
    try:                                        # 예외가 없을 경우
        A, B = input().split()                  # A 문자열 / B 순서를 input받고
        lst = list(A)                           # 문자열을 리스트로 저장하고
        visited = [0]*len(lst)                  # 방문표시를 할 리스트를 생성한다
        cnt = 1                                 # 순서를 표시할 변수를 생성하고
        flag = 0                                # 정답 여부를 표시할 변수를 생성한 후
        recur(0, '', len(lst))                  # 깊이 0부터 B번째 순열을 탐색한다
        if flag == 0:                           # flag가 0인 경우 정답이 없으므로
            print(f'{A} {B} = No permutation')  # No permutation을 출력한다
    except:                                     # 더 이상 input 값이 없다면
        break                                   # break 한다