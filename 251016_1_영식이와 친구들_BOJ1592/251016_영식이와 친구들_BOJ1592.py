# 영식이와 친구들_BOJ1592

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, L = map(int, input().split()) # 사람의수, 공을 받아야하는 횟수, 넘기는 거리를 input받고
ans = [0]*N                         # 시행횟수를 저장할 리스트를 생성하고
a = 0                               # 공을 받은 사람의 위치를 나타낼 변수를 생성하고
num = -1                            # 시행횟수를 저장할 변수를 생성한다
while 1:                            # break가 나올때까지 반복해서
    ans[a] += 1                     # 공을 받은사람의 횟수를 추가하고
    num += 1                        # 공을 던진 수를 추가한다
    if ans[a] == M:                 # 공을 받아야하는 수를 도달했다면
        break                       # while문을 종료한다
    a += L                          # 공을 다음으로 던져주고
    a %= N                          # 다음 공을 받을 사람을 계산한다
print(num)                          # 공을 던진 횟수를 출력한다