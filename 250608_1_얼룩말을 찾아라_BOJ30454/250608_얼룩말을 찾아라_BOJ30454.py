# 얼룩말을 찾아라_BOJ30454

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, L = map(int, input().split())        # 얼룩말의 줄무늬와 마리수를 input받고
Z, M = 0, 0                             # 줄무늬의 수와 개체수를 저장할 변수를 생성하고
for n in range(N):                      # 줄무늬의 세로의 수를 반복해서
    zebra = input().strip()             # 줄무늬를 input 받고
    tmp = 0                             # 줄의 색을 나타낼 변수를 생성하고
    ans = 0                             # 줄의 수를 나타낼 변수르 생성한다
    for z in zebra:                     # 줄무늬의 가로를 반복해서
        if tmp == 0 and z == '1':       # 이전이 흰줄인데 검은줄이 나왓다면
            ans += 1                    # 줄무늬의 수를 1 추가하고
            tmp = 1                     # 이전 줄을 검을 줄로 바꿔준다
        elif tmp == 1 and z == '0':     # 이전이 검은 줄인데 흰줄이 나왔다면
            tmp = 0                     # 이전 줄을 흰줄로 바꿔준다
    else:                               # 줄무늬를 모두 셋다면
        if ans > Z:                     # 현재 줄무늬가 가장 많다면
            Z = ans                     # 가장 많은 줄무늬를 저장하고
            M = 1                       # 개체수를 1로 저장한다
        elif ans == Z:                  # 줄무늬가 최대와 같다면
            M += 1                      # 개체수를 1 추가한다
print(Z, M)                             # 가장 많은 줄무늬와 개체수를 출력한다