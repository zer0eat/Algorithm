# Do Not Touch Anything_BOJ13136

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
r, c, n = map(int, input().split()) # 세로 가로 cctv 커버 길이를 input 받고
R, C = r//n, c//n                   # 세로 가로에 필요한 cctv의 수를 계산하고
if r%n:                             # cctv로 세로를 딱 맞게 커버가 안된다면
    R += 1                          # 세로의 대수를 1추가하고
if c%n:                             # cctv로 가로를 딱 맞게 커버가 안된다면
    C += 1                          # 가로의 대수를 1추가하고
print(R*C)                          # cctv의 수를 출력한다