# 붙임성 좋은 총총이_BOJ26069

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 사람들이 만난 기록의 수를 input 받고
dance = dict()                          # 사람들이 춤추고 있는 정보를 저장할 딕셔너리를 생성해서
dance['ChongChong'] = 1                 # ChongChong은 무지개 댄스를 추고 있다는 표시를 한다
for i in range(N):                      # 사람들이 만나 기록의 수를 반복해서
    a, b = input().split()              # 만난 사람의 이름을 input 받고
    if dance.get(a) or dance.get(b):    # 두사람 중 한명이라도 무지개 댄스를 추고 있다면
        dance[a] = 1                    # a가 무지개 댄스를 추고 있다는 표시를 한다
        dance[b] = 1                    # b가 무지개 댄스를 추고 있다는 표시를 한다
print(len(dance))                       # 마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력한다