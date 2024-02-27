# 영재의 시험_BOJ19949

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
questions = list(map(int, input().split()))             # 문제의 정답을 리스트롤 input 받고
ans = 0                                                 # 5점이상인 경우를 저장할 변수를 생성한다

def recur(dep, cnt, answer):
    global ans                                          # ans를 global 변수로 선언하고
    if dep == 10:                                       # 10문제를 모두 탐색했다면
        if cnt >= 5:                                    # 정답이 5개 이상일 때
            ans += 1                                    # 경우의 수를 1 추가하고
        return                                          # return한다
    if dep < 2:                                         # 깊이가 2 미만일 때
        for i in range(1, 6):                           # 1부터 5까지 반복해서
            if questions[dep] == i:                     # 정답을 맞췄다면
                cnt += 1                                # 정답의 수를 1 추가하고
            answer.append(i)                            # i를 정답리스트에 append하고
            recur(dep+1, cnt, answer)                   # 깊이 dep+1부터 맞춘개수를 탐색한다
            answer.pop()                                # i를 정답리스트에서 pop하고
            if questions[dep] == i:                     # 정답을 맞췄다면
                cnt -= 1                                # 정답의 수를 1 감소한다
    else:                                               # 깊이가 2 이상일 때
        for i in range(1, 6):                           # 1부터 5까지 반복해서
            if answer[-1] == i and answer[-2] == i:     # 이전 2개의 선택이 현재와 같다면
                continue                                # continue하고
            if questions[dep] == i:                     # 정답을 맞췄다면
                cnt += 1                                # 정답의 수를 1 추가하고
            answer.append(i)                            # i를 정답리스트에 append하고
            recur(dep+1, cnt, answer)                   # 깊이 dep+1부터 맞춘개수를 탐색한다
            answer.pop()                                # i를 정답리스트에서 pop하고
            if questions[dep] == i:                     # 정답을 맞췄다면
                cnt -= 1                                # 정답의 수를 1 감소한다

recur(0, 0, [])                                         # 깊이 0부터 맞춘개수를 세며 탐색한다
print(ans)                                              # 점수가 5점 이상일 경우의 수를 출력한다