# 회문_13755

# input.txt 열기
import sys
sys.stdin = open('input.txt')
 
# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N, M = map(int, input().split()) # 입력될 문장의 숫자
    lst = [list(input()) for _ in range(N)]
     
    # 회문찾기
    a = 0 # 회문이 될 수 있는 시작점의 인덱스를 row는 a로 col은 b로 저장한다
    b = 0
    for n in range(N): # NxN 행렬에서 가로로 탐색을 할 때 길이가 M인 회문의 시작점을 찾아 시작점을 a,b에 저장한다
        for m in range(N - M + 1):
            if lst[n][m] == lst[n][M + m -1]:
                a = n
                b = m
                # 회문을 빈리스트 c에 저장하고 길이가 M인 회문만 추출한다.
                c = []
                for mm in range(M):
                    c.append(lst[a][b+mm])
                    if c == c[::-1] and len(c) == M:
                        print(f'#{t+1}', ''.join(c))
 
    for n in range(N): # NxN 행렬에서 세로로 탐색을 할 때 길이가 M인 회문의 시작점을 찾아 시작점을 a,b에 저장한다
        for m in range(N - M + 1):
            if lst[m][n] == lst[M + m -1][n]:
                a = m
                b = n
                # 회문을 빈리스트 c에 저장하고 길이가 M인 회문만 추출한다.
                c = []
                for mm in range(M):
                    c.append(lst[a+mm][b])
                    if c == c[::-1] and len(c) == M:
                        print(f'#{t+1}', ''.join(c))






    
