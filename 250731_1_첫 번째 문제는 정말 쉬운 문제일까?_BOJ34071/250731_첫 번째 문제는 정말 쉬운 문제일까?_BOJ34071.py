# 첫 번째 문제는 정말 쉬운 문제일까?_BOJ34071

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 문제의 수를 input받고
L = []                          # 난이도를 저장할 리스트를 생성해서
for n in range(N):              # 문제의 수를 반복하고
    L.append(int(input()) )     # 리스트에 난이도를 append한다
if L.index(min(L)) == 0:        # 첫 문제가 제일 쉽다면
    print('ez')                 # ez를 출력하고
elif L.index(max(L)) == 0:      # 첫 문제가 제일 어렵다면
    print('hard')               # hard를 출력하고
else:                           # 둘 다 아니라면
    print('?')                  # ?를 출력한다