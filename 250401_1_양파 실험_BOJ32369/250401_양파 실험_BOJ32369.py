# 양파 실험_BOJ32369.py

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, A, B = map(int, input().split()) # 키운 일수와 자라는 길이를 input 받고
a, b = 1, 1                         # 양파의 길이를 변수로 생성해서
for n in range(N):                  # 키운 일수를 반복해서
    a += A                          # 칭찬 양파를 키우고
    b += B                          # 비난 양파를 키워서
    if a < b:                       # 비난 양파가 더 크다면
        a, b = b, a                 # 둘을 바꾸고
    elif a == b:                    # 길이가 같다면
        b -= 1                      # 비난 양파를 1 자른다
print(a, b)                         # 칭찬 양파와 비난 양파를 출력한다