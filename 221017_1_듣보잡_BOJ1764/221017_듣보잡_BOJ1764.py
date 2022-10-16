# 듣보잡_BOJ1764

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())       # N 듣도 못한 사람의 수 / M 보도 못한 사람의 수

unheard = set()                                     # 듣도 못한 사람을 저장할 set 생성
for n in range(N):                                  # 듣도 못한 사람의 수만큼 반복해서
    q = sys.stdin.readline().rstrip()               # q에 듣도 못한 사람을 저장하고
    unheard.add(q)                                  # unheard set에 add

unseen = set()                                      # 보도 못한 사람을 저장할 set 생성
for m in range(M):                                  # 보도 못한 사람의 수만큼 반복해서
    q = sys.stdin.readline().rstrip()               # q에 보도 못한 사람을 저장하고
    unseen.add(q)                                   # unseen set에 add

unheardseen = unheard & unseen                      # 두 set의 교집합을 구해 듣도 보도 못한사람을 구한 후
unheardseen = list(unheardseen)                     # 리스트로 변경해서
unheardseen.sort()                                  # 사전순으로 정렬한다

print(len(unheardseen))                             # 듣도 보도 못한사람의 수를 출력하고
for u in unheardseen:                               # 사전 순으로 이름을 출력한다
    print(u)