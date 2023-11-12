# 풍선 터뜨리기_BOJ2346

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 풍선의 개수를 input 받고
A = list(map(int, input().split()))     # 풍선 속에 있는 이동횟수를 리스트로 input 받는다
balloon = [i for i in range(1, N+1)]    # 풍선을 순서대로 넣은 리스트를 생성하고
cnt = A[0]                              # 이동횟수를 cnt에 저장하고
ans = [1]                               # 터진 풍선의 번호를 저장할 리스트를 생성하고
balloon[0] = 0                          # 첫번째 풍선을 터트린 후
idx = 0                                 # 이동을 위한 위치를 나타낼 변수를 생성한다
while sum(balloon):                     # 풍선이 모두 터질 때까지 반복해서
    if cnt > 0:                         # 이동 횟수가 양수라면
        idx = (idx+1) % N               # 인덱스를 오른쪽으로 이동한 값으로 저장하고
        if balloon[idx]:                # 이동한 칸의 풍선이 남아 있다면
            cnt -= 1                    # 이동횟수를 하나 감소한다
    elif cnt < 0:                       # 이동 횟수가 음수라면
        idx = (idx - 1) % N             # 인덱스를 왼쪽으로 이동한 값으로 저장하고
        if balloon[idx]:                # 이동한 칸의 풍선이 남아 있다면
            cnt += 1                    # 이동횟수를 하나 감소한다
    else:                               # 이동 횟수가 남아 있지 않다면
        ans.append(idx+1)               # 터진 풍선을 ans에 append하고
        cnt = A[idx]                    # cnt에 이동횟수를 저장한 후
        balloon[idx] = 0                # 풍선을 터짐 표시한다
print(*ans)                             # 터진 풍선의 번호를 차례대로 출력한다