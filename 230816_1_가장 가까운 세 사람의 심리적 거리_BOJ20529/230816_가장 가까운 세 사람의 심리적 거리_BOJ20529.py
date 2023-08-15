# 가장 가까운 세 사람의 심리적 거리_BOJ20529

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복해서
    N = int(input())                                # 학생의 수를 input받고
    MBTI = list(input().split())                    # N명의 학생의 MBTI를 리스트로 input 받는다
    if N > 32:                                      # 학생의 수가 32명 초과인 경우
        print(0)                                    # 적어도 1가지 경우의 MBTI가 3종류가 겹치므로 0을 출력한다
    else:                                           # 학생의 수가 32명 이하인 경우
        ans = 12                                    # 3명의 MBTI의 최소 차이를 저장할 변수를 생성하고
        for lst in combinations(MBTI, 3):           # MBTI의 리스트 중 3명씩 조합으로 반복해서
            tmp = 0                                 # 3명의 차이를 저장할 변수를 저장하고
            for i in range(2):                      # 3명의 조합 중 앞에 두명을 반복하고
                for j in range(i + 1, 3):           # i번 이후를 반복해서
                    for k in range(4):              # MBTI의 4가지 척도를 반복해서
                        if lst[i][k] != lst[j][k]:  # 다른 경우에는
                            tmp += 1                # tmp에 1을 더한다
            else:                                   # 3명의 MBTI를 모두 비교했다면
                ans = min(tmp, ans)                 # tmp와 ans 중 더 작은 값을 ans에 저장한다
        print(ans)                                  # 모든 조합을 마친 후 가장 가까운 세 학생 사이의 심리적인 거리를 출력한다