# 출석이벤트_BOJ25704

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
B = int(input())            # 쿠폰의 개수를 input 받고
P = int(input())            # 가격을 input 받는다
ans = P                     # 정답을 저장할 변수를 생성하고
if B >= 5:                  # 쿠폰이 5개 이상이면
    ans = P-500             # P에서 500원을 뺀 금액을 저장한다
if B >= 10:                 # 쿠폰이 10개 이상이면
    ans = min(ans, P*0.9)   # ans와 10% 할인 금액중 작은 값을 저장한다
if B >= 15:                 # 쿠폰이 15개 이상이면
    ans = min(ans, P-2000)  # ans와 2000원을 뺀 금액중 작은 값을 저장한다
if B >= 20:                 # 쿠폰이 20개 이상이면
    ans = min(ans, P*0.75)  # ans와 20% 할인 금액중 작은 값을 저장한다
if ans < 0:                 # 가격이 0보다 작다면
    print(0)                # 0원을 출력한다
else:                       # 가격이 0 이상이라면
    print(int(ans))         # 최저가격을 출력한다