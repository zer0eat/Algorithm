# 편의점2_BOJ14400

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input.txt 열기
N = int(input())                        # 고객의 수를 input 받고
x = []                                  # 고객의 x 위치를 저장할 리스트를 생성하고
y = []                                  # 고객의 y 위치를 저장할 리스트를 생성한다
for n in range(N):                      # 고객의 수를 반복해서
    a, b = map(int, input().split())    # 고객의 x,y 위치를 a,b에 input 받고
    x.append(a)                         # a를 x 리스트에 더하고
    y.append(b)                         # b를 y 리스트에 더한다
x.sort()                                # 고객의 x 위치를 오름차순 정렬하고
y.sort()                                # 고객의 y 위치를 오름차순 정렬한 후
ans = 0                                 # 고객의 거리를 저장할 변수를 생성하고
for i in range(N):                      # 고객의 수를 반복해서
    ans += abs(x[i]-x[N//2])            # 고객의 위치와 편의점의 x 거리의 차를 더하고
    ans += abs(y[i]-y[N//2])            # 고객의 위치와 편의점의 y 거리의 차를 더해서
print(ans)                              # 모든 고객들의 거리 합을 최소로 하는 합을 출력한다