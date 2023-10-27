# 톱니바퀴_BOJ14891

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
gear = [deque(input().strip()) for _ in range(4)]   # 4개의 톱니바퀴의 상태를 input 받고

def rotation(num, d):
    visited = [0] * 4                               # 회전할 기어를 표시할 리스트를 생성하고
    # 돌아갈 기어 선택
    visited[num] = 1                                # num 기어를 돌아갈 기어로 표시한다
    for i in range(num, 0, -1):                     # num의 왼쪽에 있는 기어를 반복해서
        if gear[i-1][2] != gear[i][6]:              # 왼쪽기어의 오른쪽 톱니와 오른쪽기어의 왼쪽 톱니가 서로 상극이라면
            visited[i-1] = 1                        # 왼쪽기어를 방문표시한다
        else:                                       # 왼쪽기어의 오른쪽 톱니와 오른쪽기어의 왼쪽 톱니가 서로 같은 극이라면
            break                                   # 이후로 회전이 불가능하므로 for문을 break한다
    for i in range(num, 3):                         # num의 오른쪽에 있는 기어를 반복해서
        if gear[i][2] != gear[i+1][6]:              # 왼쪽기어의 오른쪽 톱니와 오른쪽기어의 왼쪽 톱니가 서로 상극이라면
            visited[i+1] = 1                        # 오른쪽기어를 방문표시한다
        else:                                       # 왼쪽기어의 오른쪽 톱니와 오른쪽기어의 왼쪽 톱니가 서로 같은 극이라면
            break                                   # 이후로 회전이 불가능하므로 for문을 break한다
    # 기어 돌리기
    for i in range(4):                              # 기어를 반복해서
        if visited[i] == 1:                         # i번째 기어가 회전할 기어라면
            if i % 2 == num % 2:                    # i번째 기어가 num 기어가 짝수개 차이라면
                if d > 0:                           # num이 시계방향으로 돈다면 i번째도 시계방향으로 돌게 되므로
                    a = gear[i].pop()               # 기어의 맨 뒤 숫자를 pop해서
                    gear[i].appendleft(a)           # 기어의 맨 앞으로 appendleft한다
                else:                               # num이 반시계방향으로 돈다면 i번째도 반시계방향으로 돌게 되므로
                    a = gear[i].popleft()           # 기어의 맨 앞 숫자를 popleft해서
                    gear[i].append(a)               # 기어의 맨 뒤로 append한다
            else:                                   # i번째 기어가 num 기어가 홀수개 차이라면
                if d > 0:                           # num이 시계방향으로 돈다면 i번째는 반시계방향으로 돌게 되므로
                    a = gear[i].popleft()           # 기어의 맨 앞 숫자를 popleft해서
                    gear[i].append(a)               # 기어의 맨 뒤로 append한다
                else:                               # num이 반시계방향으로 돈다면 i번째는 시계방향으로 돌게 되므로
                    a = gear[i].pop()               # 기어의 맨 뒤 숫자를 pop해서
                    gear[i].appendleft(a)           # 기어의 맨 앞으로 appendleft한다

K = int(input())                                    # 회전할 수를 input 받고
for k in range(K):                                  # 회전할 수를 반복해서
    num, d = map(int, input().split())              # num 회전할 기어번호 / d 회전하는 방향을 input 받고
    rotation(num-1, d)                              # rotation 함수를 통해 기어를 돌린다
ans = 0                                             # 정답을 저장할 변수를 생성하고
for i in range(4):                                  # 기어를 반복해서
    if gear[i][0] == '1':                           # 기어의 12시방향이 S극이라면
        ans += 2**i                                 # ans에 점수를 더한다
print(ans)                                          # K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다