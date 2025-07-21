# 배스킨라빈스 31_BOJ14429

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 게임의 수를 input받고
ans, turn = 0, 100000                   # 정답과 턴수를 저장할 변수를 생성한다
for n in range(N):                      # 게임의 수를 반복해서
    j, m = map(int, input().split())    # 부르면 안되는 수와 최대로 부를 수 있는 수를 input받고
    r = (j-1) % (1+m)                   # 필승 숫자를 계산해서 저장하고
    tmp, num = 1, r                     # 턴과 현재 숫자를 저장한다
    flag = False                        # 규용이의 차례로 변수를 생성한다
    while num < j:                      # 부르면 안되는 숫자가 나올때까지 반복해서
        if flag:                        # 유진이의 차례라면
            flag = False                # 규용이의 차례로 변수를 변경하고
            tmp += 1                    # 턴을 추가하고
            num += r - (num%(1+m))      # 필승 숫자로 맞춰준다
        else:                           # 규용이의 차례라면
            flag = True                 # 유진이의 차례로 변수를 변경하고
            tmp += 1                    # 턴을 추가하고
            num += m                    # 최대로 부를 수 있는 수를 더해준다
    if tmp < turn:                      # 최소 턴이 나왔다면
        turn = tmp                      # 최소 턴을 저장하고
        ans = n+1                       # 게임 순서를 저장하고
print(ans, turn)                        # 게임순서와 턴을 출력한다