# 숨바꼭질_BOJ1697

# import.txt 열기
import sys
sys.setrecursionlimit(1000000)                   # 재귀의 깊이를 1000000으로 설정해준 후
sys.stdin = open('input.txt')

def hide_and_seek(lst):
    global cnt, K                               # 시간을 카운트하는 변수와 수빈이 동생의 위치를 불러오고
    next = []                                   # 다음 시간에 수빈이가 이동할 위치를 저장할 빈 리스트를 생성
    for n in lst:                               # 이번 시간에 방문할 리스트를 반복해서
        try:                                    # 딕셔너리에 key값으로 현재 위치가 저장되어 있다면
            time[n]                             # 이미 방문한 곳이므로 넘어가고
        except:                                 # 딕셔너리에 key값으로 현재 위치가 저장되어 있지 않다면
            time[n] = cnt                       # 현재 시간을 value로 딕셔너리에 저장하고
            next.append(n - 1)                  # 다음에 방문할 리스트에 다음에 갈수 있는 n-1을 append
            if n + 1 <= 100000:                 # 다음 위치가 100000이 넘을 수 없으므로 이보다 작다면
                next.append(n + 1)              # 다음에 방문할 리스트에 다음에 갈수 있는 n+1을 append
            if n * 2 <= 100000:                 # 다음 위치가 100000이 넘을 수 없으므로 이보다 작다면
                next.append(n * 2)              # 다음에 방문할 리스트에 다음에 갈수 있는 n*2을 append
        if n == K:                              # 현재 방문한 곳이 동생이 있는 곳이라면
            print(time[n])                      # 걸린 시간을 출력하고
            quit()                              # 종료한다
    cnt += 1                                    # 리스트를 모두 반복해도 동생의 위치에 도달하지 못했다면 시간을 1 증가시키고
    hide_and_seek(next)                         # 다음 방문지점의 리스트를 가지고 숨바꼭질 함수를 탐색한다
    return

# input 받기
N, K = map(int, sys.stdin.readline().split())   # N 수빈이의 위치 / K 수빈이 동생의 위치

time = dict()                                   # 매 초마다 수빈이가 있는 위치를 key로 시간을 value로 저장할 딕셔너리 생성
cnt = 0                                         # 시간을 카운트할 변수 생성

hide_and_seek([N])                              # 숨바꼭질을 하는 함수를 수빈이가 있는 위치를 시작으로 탐색


