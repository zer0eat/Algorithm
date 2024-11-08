# Арифметическая магия_BOJ18096

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 계수를 입력받고
x, y = 1, 1                                 # x, y의 수를 저장하고
ans = (x*y + x + y + 1 - x*y - x - y)**N    # 정답을 계산한 후
print(ans)                                  # 정답을 출력한다