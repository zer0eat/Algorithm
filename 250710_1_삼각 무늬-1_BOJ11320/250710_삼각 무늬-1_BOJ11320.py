# 삼각 무늬-1_BOJ11320

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input받고
for t in range(T):                      # 테스트 케이스를 반복해서
    A, B = map(int, input().split())    # 삼각형의 두변을 input받고
    ans = 0                             # 정답을 저장할 변수를 생성해서
    for a in range(A//B):               # 한변에 들어갈 삼각형의 수를 반복해서
        ans += 1 + 2*a                  # 삼각형의 수를 더해주고
    print(ans)                          # 정답을 출력한다