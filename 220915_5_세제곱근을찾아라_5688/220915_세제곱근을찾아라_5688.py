# 세제곱근을찾아라_5688

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                        # 테스트 케이스
for t in range(T):                      # 테스트 케이스를 반복할 때
    N = int(input())                    # 세제곱이 N이 되는 수를 input 받고
    A = 1                               # A를 1로 변수를 생성한 후
    while 1:                            # break 될때까지 반복해서
        if A**3 == N:                   # A의 3제곱이 N이 되면
            print(f'#{t+1}', A)         # A를 출력하고
            break                       
        elif A**3 > N:                  # A의 3제곱이 N을 넘어서면
            print(f'#{t+1}', -1)        # -1을 출력하고
            break
        else:                           # A의 3제곱이 N보다 작다면
            A += 1                      # A에 1을 더하고 다시 반복한다
