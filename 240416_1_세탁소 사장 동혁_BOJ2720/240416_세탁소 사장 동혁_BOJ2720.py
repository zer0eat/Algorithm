# 세탁소 사장 동혁_BOJ2720

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                # 테스트 케이스 input 받고
for t in range(T):              # 테스트 케이스를 반복해서
    ans = [0] * 4               # 정답을 저장할 리스트를 생성한다
    money = int(input())        # 거스름돈을 input 받고
    for n in range(4):          # 4개의 동전을 반복해서
        if n == 0:              # 첫번째 경우라면
            ans[n] = money//25  # 25센트로 줄 수 있는 개수를 리스트 맨 앞에 저장하고
            money = money%25    # 25센트를 주고 난 나머지를 변수에 저장한다
        elif n == 1:            # 두번째 경우라면
            ans[n] = money//10  # 10센트로 줄 수 있는 개수를 리스트 맨 앞에 저장하고
            money = money%10    # 10센트를 주고 난 나머지를 변수에 저장한다
        elif n == 2:            # 세번째 경우라면
            ans[n] = money//5   # 5센트로 줄 수 있는 개수를 리스트 맨 앞에 저장하고
            money = money%5     # 5센트를 주고 난 나머지를 변수에 저장한다
        else:                   # 남은 거스름돈은
            ans[n] = money      # 리스트 마지막 원소에 저장한다
    print(*ans)                 # 필요한 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 출력한다