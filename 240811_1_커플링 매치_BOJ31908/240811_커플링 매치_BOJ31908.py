# 커플링 매치_BOJ31908

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 사람의 수를 input 받고
couple = dict()                     # 커플링을 저장할 딕셔너리를 생성한다
for n in range(N):                  # 사람의 수를 반복해서
    name, ring = input().split()    # 사람의 이름과 반지의 종류를 input 받고
    if ring == '-':                 # 반지를 끼고있지 않다면
        continue                    # continue로 넘어가고
    if couple.get(ring) == None:    # 같은 반지를 낀사람이 없다면
        couple[ring] = [name]       # 반지를 키로 만들어서 리스트에 사람이름을 담아 저장한다
    else:                           # 같은 반지를 낀사람이 있다면
        couple[ring].append(name)   # 반지가 키인 원소에 사람 이름을 append한다
ans = 0                             # 커플의심군의 수를 저장할 변수를 생성하고
ans2 = []                           # 커플의심군의 이름을 저장할 리스트를 생성한다
for c in couple:                    # 커플링의 정보를 반복해서
    if len(couple[c]) == 2:         # 같은 커플링을 낀사람이 두명이라면
        ans += 1                    # 커플의심군을 1 추가하고
        ans2.append(couple[c])      # 커플의심군의 이름을 리스트에 append한다
print(ans)                          # 커플의심군의 수를 출력하고
for a in ans2:                      # 커플의심군의 이름을 반복해서
    print(*a)                       # 커플의심군의 매칭이 되는 2명을 출력한다