# 통학의 신_BOJ17945

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 이차방정식의 계수와 상수를 input 받고
ans = []                            # 정답을 저장할 리스트를 생성한다
for i in range(-1000, 1001):        # -1000부터 1000까지 반복해서
    if i**2+A*2*i+B == 0:           # 이차방정식의 해가 되는 i가 나오면
        ans.append(i)               # ans에 append하고
print(*ans)                         # 방정식의 근을 출력한다