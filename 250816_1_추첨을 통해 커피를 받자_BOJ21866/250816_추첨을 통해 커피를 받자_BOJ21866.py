# 추첨을 통해 커피를 받자_BOJ21866

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
Q = list(map(int, input().split())) # 문제의 점수를 input받고
ans = 0                             # 정답을 저장할 변수를 생성하고
for q in range(9):                  # 문제의 수를 반복해서
    if q < 2:                       # 1번 2번 문제라면
        if Q[q] > 100:              # 점수가 100점보다 크다면
            print('hacker')         # hacker를 출력하고
            quit()                  # 종료한다
        else:                       # 점수가 100점 이하라면
            ans += Q[q]             # 변수에 점수를 추가한다
    elif q < 4:                     # 3번 4번 문제라면
        if Q[q] > 200:              # 점수가 200점보다 크다면
            print('hacker')         # hacker를 출력하고
            quit()                  # 종료한다
        else:                       # 점수가 200점 이하라면
            ans += Q[q]             # 변수에 점수를 추가한다
    elif q < 6:                     # 5번 6번 문제라면
        if Q[q] > 300:              # 점수가 300점보다 크다면
            print('hacker')         # hacker를 출력하고
            quit()                  # 종료한다
        else:                       # 점수가 300점 이하라면
            ans += Q[q]             # 변수에 점수를 추가한다
    elif q < 8:                     # 7번 8번 문제라면
        if Q[q] > 400:              # 점수가 400점보다 크다면
            print('hacker')         # hacker를 출력하고
            quit()                  # 종료한다
        else:                       # 종점수가 400점 이하라면
            ans += Q[q]             # 변수에 점수를 추가한다
    else:                           # 9번 문제라면
        if Q[q] > 500:              # 점수가 500점보다 크다면
            print('hacker')         # hacker를 출력하고
            quit()                  # 종료한다
        else:                       # 점수가 500점 이하라면
            ans += Q[q]             # 변수에 점수를 추가한다
if ans >= 100:                      # 점수 총 합이 100점 이상이라면
    print('draw')                   # draw를 출력한다
else:                               # 점수 총 합이 100점 이하라면
    print('none')                   # none을 출력한다