# 샤틀버스_BOJ25625

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
x, y = map(int, input().split())    # 지하철과 버스의 시간을 input 받고
if x < y:                           # 지하철이 버스보다 늦게오면
    t = x // y + 1                  # 그 다음 버스가 올 시간을 구해서
    print(y*t-x)                    # 시간을 출력한다
else:                               # 지하철이 버스보다 빠르게 오면
    print(x+y)                      # 두 시간을 합한 결과를 출력한다