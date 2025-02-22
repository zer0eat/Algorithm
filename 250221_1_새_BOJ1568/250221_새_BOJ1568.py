# 새_BOJ1568

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 새의 수를 input 받고
ans = 0             # 정답을 저장할 변수를 생성해서
bird = 1            # 날아가는 새의 수를 저장할 변수를 생성한다
while 1:            # 종료할 때까지 반복해서
    if N >= bird:   # 날아가는 새보다 같거나 더 많이 남았다면
        ans += 1    # 1초를 추가하고
        N -= bird   # 새를 날린 후
        bird += 1   # 다음 날아갈 새를 추가한다
    else:           # 나랑가는 새보다 적게 남았다면
        bird = 1    # 새를 초기화하고
    if N == 0:      # 모두 날아갔다면
        print(ans)  # 지나간 시간을 출력하고
        quit()      # 종료한다