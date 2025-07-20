# 관리자는 누구?_BOJ14724

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 동아리원의 수를 input받고
G = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY'] # 동아리명을 리스트로 저장해서
ans = []                                    # 푼 문제의 수를 저장할 리스트를 생성하고
for g in range(9):                          # 동아리의 수를 반복해서
    L = list(map(int, input().split()))     # 동아리원의 푼문제를 input받고
    ans.append(max(L))                      # 가장 많이 푼사람의 문제를 리스트에 append한다
print(G[ans.index(max(ans))])               # 가장 많이 푼사람이 속한 동아리를 출력한다