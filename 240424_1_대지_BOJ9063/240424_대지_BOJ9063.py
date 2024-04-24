# 대지_BOJ9063

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 점의 개수를 input 받고
x = []                                  # x 축의 점을 저장할 리스트를 생성하고
y = []                                  # y 축의 점을 저장할 리스트를 생성한다
for n in range(N):                      # 점의 개수를 반복해서
    a, b = map(int, input().split())    # a,b의 점을 input 받고
    x.append(a)                         # x에 a를 append하고
    y.append(b)                         # y에 b를 append한다
print((max(x)-min(x))*(max(y)-min(y)))  # N개의 점을 둘러싸는 최소 크기의 직사각형의 넓이를 출력한다