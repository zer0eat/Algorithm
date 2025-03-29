# 준영이의 등급_BOJ30008

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())        # 학생의 수, 과목의 수를 input 받고
rank = list(map(int, input().split()))  # 과목의 등수를 리스트로 input 받고
ans = []                                # 정답을 저장할 리스트를 생성한다
for k in range(K):                      # 과목의 수를 반복해서
    P = int(rank[k]/N * 100)            # 과목의 퍼센트를 구해서
    if 0 <= P and P <= 4:               # 0이상 4이하라면
        ans.append(1)                   # 1등급을 추가하고
    elif 4 < P and P <= 11:             # 4초과 11이하라면
        ans.append(2)                   # 2등급을 추가하고
    elif 11 < P and P <= 23:            # 11초과 23이하라면
        ans.append(3)                   # 3등급을 추가하고
    elif 23 < P and P <= 40:            # 23초과 40이하라면
        ans.append(4)                   # 4등급을 추가하고
    elif 40 < P and P <= 60:            # 40초과 60이하라면
        ans.append(5)                   # 5등급을 추가하고
    elif 60 < P and P <= 77:            # 60초과 77이하라면
        ans.append(6)                   # 6등급을 추가하고
    elif 77 < P and P <= 89:            # 77초과 89이하라면
        ans.append(7)                   # 7등급을 추가하고
    elif 89 < P and P <= 96:            # 89초과 96이하라면
        ans.append(8)                   # 8등급을 추가하고
    elif 96 < P and P <= 100:           # 96초과 100이하라면
        ans.append(9)                   # 9등급을 추가하고
print(*ans)                             # 정답을 출력한다