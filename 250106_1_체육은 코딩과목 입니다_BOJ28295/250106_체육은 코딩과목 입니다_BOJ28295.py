# 체육은 코딩과목 입니다_BOJ28295

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                                 # 방향을 나타낼 변수를 생성하고
direction = {1:'E',2:'S',3:'W',0:'N'}   # 방향을 변환할 딕셔너리를 생성한다
for n in range(10):                     # 10번을 반복해서
    num = int(input())                  # 지시할 명령을 input 받고
    if num == 1:                        # 1이 나오면
        ans += 1                        # 우향우를 하고
        ans %= 4                        # 4방향으로 정리한다
    elif num == 2:                      # 2가 나오면
        ans += 2                        # 뒤로 돌아를 하고
        ans %= 4                        # 4방향으로 정리한다
    else:                               # 3이 나오면
        ans -= 1                        # 좌향좌를 해서
        if ans < 0:                     # 음수라면
            ans = 3                     # 4방향으로 정리한다
print(direction[ans])                   # 마지막으로 바라보고 있는 방향을 출력한다