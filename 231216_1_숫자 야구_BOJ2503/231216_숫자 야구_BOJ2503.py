# 숫자 야구_BOJ2503

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import permutations
from copy import deepcopy

# input 받기
N = int(input())                                                    # 질문의 횟수를 input받고
balls = ['1','2','3','4','5','6','7','8','9']                       # 숫자 야구를 위해 필요한 숫자 리스트를 생성하고
ans = [ball for ball in permutations(balls,3)]                      # 1부터 9개의 숫자를 골라 순열 조합을 리스트에 저장한다
for n in range(N):                                                  # 질문 횟수를 반복해서
    baseball = list(input().split())                                # 질문한 3자리 조합과 스트라이크와 볼의 개수를 리스트로 input 받고
    ans2 = []                                                       # 질문을 통과한 순열 조합을 저장할 리스트를 생성한다
    for ball in ans:                                                # 순열 조합 리스트를 반복해서
        s = 0                                                       # 스트라이크의 숫자를 저장할 변수를 생성하고
        b = 0                                                       # 볼의 숫자를 저장할 변수를 생성해서
        for i in range(3):                                          # 질문한 3자리를 반복했을 때
            if ball[i] == baseball[0][i]:                           # 질문한 자리와 순열조합의 자리의 숫자가 일치한다면
                s += 1                                              # 스트라이크의 수를 추가하고
            elif ball[i] in baseball[0]:                            # 질문한 자리와 순열조합의 자리의 숫자가 일치하지 않을 때 순열조합의 해당자리의 원소가 질문에 포함된다면
                b += 1                                              # 볼의 수를 추가하고
        else:                                                       # 모든 자리를 확인했다면
            if str(s) == baseball[1] and str(b) == baseball[2]:     # 스트라이크와 볼의 수가 input받은 내용과 일치할 경우
                ans2.append(ball)                                   # 해당 순열조합을 ans2에 append한다
    else:                                                           # 모든 순열조합을 반복했다면
        ans = deepcopy(ans2)                                        # 질문을 통과한 순열조합을 담은 ans2를 ans에 저장한다
print(len(ans))                                                     # 숫자야구의 정답으로 생각하고 있을 가능성이 있는 답의 총 개수를 출력한다