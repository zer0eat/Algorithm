# 아름다운 수_BOJ2774

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())        # 테스트 케이스를 input받고
for t in range(T):      # 테스트 케이스를 반복해서
    ans = [0]*10        # 정답을 저장할 리스트를 생성하고
    X = input().strip() # 숫자를 input받고
    for x in X:         # 숫자의 각 자리수를 반복해서
        ans[int(x)] = 1 # 나온 숫자의 종류를 표시하고
    print(sum(ans))     # 숫자 종류의 합을 출력한다