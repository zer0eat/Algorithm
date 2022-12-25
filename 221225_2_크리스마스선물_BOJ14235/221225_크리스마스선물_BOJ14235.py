# 크리스마스선물_BOJ14235

# input 열기
import sys
sys.stdin = open('input.txt')

# input 받기
n = int(sys.stdin.readline().strip())                   # n 아이들과 거점을 방문한 횟수
gift = []                                               # 선물의 가치를 저장할 리스트 생성

for _ in range(n):                                      # 아이들과 거점을 방문한 횟수를 반복해서
    a = list(map(int, sys.stdin.readline().split()))    # 숫자를 리스트 형태로 input 받아서
    if a == [0]:                                        # 받은 리스트가 0인 경우에는 아이들을 방문한 것이기에
        if len(gift):                                   # 선물이 있으면
            print(gift.pop())                           # 가장 큰 가치의 선물을 출력하고
        else:                                           # 선물이 없으면
            print(-1)                                   # -1을 출력한다
    else:                                               # 받은 리스트가 0이 아닌 경우에는 거점을 방문한 것이기에
        for g in range(a[0]):                           # 저장할 선물의 수만큼 반복해서
            gift.append(a[g+1])                         # gift 리스트에 선물을 append 한 후
        gift.sort()                                     # 오름차순으로 정렬한다