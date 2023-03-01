# 스텔라가치킨을선물했어요_BOJ15905

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # N 참가자의 수
lst = [list(map(int,input().split())) for _ in range(N)]    # 맞힌문제와 패널티를 리스트형태로 lst리스트에 저장
lst.sort(reverse=True)                                      # lst를 내림차순으로 정렬

ans = 0                                                     # 정답을 저장할 변수 생성
minsolve = lst[4][0]                                        # 5번째 수상자의 푼 문제 저장
for a in range(5, N):                                       # 6번째부터 끝까지 반복해서
    if lst[a][0] == minsolve:                               # 5번째 수상자와 푼 문제가 같다면
        ans += 1                                            # ans에 1을 추가하고
    else:                                                   # 이보다 적다면
        break                                               # for문을 종료한다

print(ans)                                                  # 5번째 수상자와 푼문제의 수가 같은 사람을 출력한다