# 라디오_BOJ3135

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # A 처음 주파수 / B 바꿀 주파수
ans = abs(A - B)                    # ans에 처음 주파수에서 바꿀 주파수로 이동하는데 눌러야할 버튼 수를 저장하고
N = int(input())                    # 즐겨찾기 한 숫자를 input 받고
for n in range(N):                  # 즐겨찾기 한 숫자를 반복해서
    C = int(input())                # C에 즐겨찾기한 주파수를 저장한 후
    if ans > (abs(B - C) + 1):      # 즐겨찾기 주파수에서 B까지 눌러야할 버튼수가 ans보다 작다면
        ans = (abs(B - C) + 1)      # ans를 즐겨찾기 주파수에서 B까지 눌러야할 버튼수로 갱신하고
print(ans)                          # 모든 탐색을 마친 후 최저 버튼 수를 출력한다