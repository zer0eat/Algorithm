# 나누기_BOJ1075

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 나눠야하는 수를 input 받고
F = int(input())        # 나눌 수를 input 받는다
front = N // 100        # 100의 자리 이상만 저장하고
ans = front * 100       # ans에 N에 십의 자리 이하를 모두 0으로 만든 수를 저장한다
while ans % F != 0:     # ans가 F로 나눠떨어지지 않는다면
    ans += 1            # ans에 1을 추가한다
print(str(ans)[-2:])    # F로 나누어 떨어지는 가장 작은 자연수의 10의자리 수까지 출력한다