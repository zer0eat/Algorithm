# 숨바꼭질2_BOJ12851

# import.txt 열기
import sys
sys.setrecursionlimit(1000000)                      # 재귀의 깊이를 1000000으로 설정해준 후
sys.stdin = open('input.txt')

def hide_and_seek(lst):
    global cnt, K, num, flag                        # 시간을 카운트하는 변수/ 수빈이 동생의 위치/ 동생을 찾는 경우의 수/ 찾았을 경우 함수를 종료할 변수를 불러오고
    next = []                                       # 다음 시간에 수빈이가 이동할 위치를 저장할 빈 리스트를 생성
    for l in lst:                                   # 이번 시간에 방문할 리스트를 반복해서
        if time.get(l) == None:                     # 방문하지 않았던 곳이라면
            time[l] = cnt                           # 현재 시간을 value로 딕셔너리에 저장하고
        for x in [l - 1, l + 1, l * 2]:             # 다음에 갈 수 있는 위치를 반복해서
            if x == K:                              # 다음에 갈 수 있는 곳이 동생의 위치라면
                flag = True                         # 함수를 종료하기 위해 flag를 True로 바꾸고
                num += 1                            # 찾은 경우의 수를 1증가시킨다
            if time.get(x) == None and 0 < x <= 100001:     # 다음에 갈 곳이 방문 전이고 0부터 100001 사이의 값이라면
                next.append(x)                      # next에 append 한다
    else:                                           # 방문할 리스트를 모두 반복했다면
        if flag == True:                            # flag가 True인 경우에는
            print(cnt + 1)                          # 걸린 시간을 출력하고
            print(num)                              # 도착하는 경우의 수를 출력하고
            return                                  # 함수를 return
        else:                                       # flag가 False라면
            cnt += 1                                # cnt를 1 증가시키고
            hide_and_seek(next)                     # 다음에 방문할 리스트인 next를 가지고 숨바꼭질 함수를 탐색한다
            return

# input 받기
N, K = map(int, sys.stdin.readline().split())       # N 수빈이의 위치 / K 수빈이 동생의 위치

time = dict()                                       # 매 초마다 수빈이가 있는 위치를 key로 시간을 value로 저장할 딕셔너리 생성
cnt = 0                                             # 시간을 카운트할 변수 생성
num = 0                                             # 동생을 찾는 경우의 수를 셀 변수 생성
flag = False                                        # 동생을 찾았을 경우 함수를 종료할 변수 생성

if N == K:                                          # 수빈이와 동생이 같은 지점에 있을 때
    print(0)                                        # 0초 후에 찾는 경우의 수는 1을 출력한다
    print(1)
else:                                               # 수빈이와 동생이 다른 지점에 있을 때
    hide_and_seek([N])                              # 숨바꼭질을 하는 함수를 수빈이가 있는 위치를 시작으로 탐색