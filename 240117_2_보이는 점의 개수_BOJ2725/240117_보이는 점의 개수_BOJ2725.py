# 보이는 점의 개수_BOJ2725

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = set([1, 0, 1e9])          # 정답을 저장할 set을 생성하고
visited = [0] * 1001            # 1부터 1000범위의 점의 개수를 저장할 리스트를 생성한다
visited[1] = 3                  # 범위가 1일 때 보이는 점이 3개이므로
cnt = 2                         # 범위를 나타낼 변수를 생성하고
while cnt < 1001:               # 범위가 1000이 넘을때까지 반복해서
    for i in range(1, cnt+1):   # 1부터 cnt까지 점을 반복해서
        ans.add(cnt/i)          # i, cnt의 기울기를 ans에 add하고
        ans.add(i/cnt)          # cnt, i의 기울기를 ans에 add한다
    else:                       # 모든 점의 기울기를 구했다면
        visited[cnt] = len(ans) # cnt의 인덱스에 보이는 점의 개수를 저장하고
        cnt += 1                # 범위를 1 증가한다
C = int(input())                # 테스트 케이스를 input 받고
for c in range(C):              # 테스트 케이스를 반복해서
    N = int(input())            # 범위를 input 받고
    print(visited[N])           # 해당범위에서 보이는 점의 수를 출력한다