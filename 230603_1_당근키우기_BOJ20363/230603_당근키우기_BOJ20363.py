# 당근키우기_BOJ20363

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X, Y = map(int, input().split())  # X 온기의 값 / Y 수분의 값
if X >= Y:                        # 필요한 온기의 값이 수분의 값보다 크다면
  x = X + (Y // 10)               # x에 필요한 온기와 수분에 따른 감소하는 온기의 값을 더한다
  print(x + Y)                    # 당근이 자라기 위한 온기의 값과 수분의 값의 합을 출력한다
else:                             # 필요한 온기의 값이 수분의 값보다 작다면
  y = Y + (X // 10)               # y에 필요한 수분과 온기에 따른 감소하는 수분의 값을 더한다
  print(X + y)                    # 당근이 자라기 위한 온기의 값과 수분의 값의 합을 출력한다