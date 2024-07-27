# 브실이의 입시전략_BOJ29723

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, K = map(int, input().split()) # N 과목의 수 M 수강할 과목 K 필수과목을 input 받고
d = dict()                          # 과목의 이름과 성적을 저장할 딕셔너리를 생성한다
for n in range(N):                  # 과목의 수를 반복해서
    a, b = input().split()          # 과목 이름과 점수를 input 받고
    d[a] = int(b)                   # 과목이름을 key로 점수를 value로 input 받는다
ans = 0                             # 정답을 저장할 변수를 생성하고
for k in range(K):                  # 필수과목의 수를 반복해서
    tmp = input().strip()           # 필수과목을 input 받고
    ans += d[tmp]                   # 필수과목의 점수를 더해준 후
    del d[tmp]                      # 필수과목을 과목 딕셔너리에서 삭제한다
l = list()                          # 리스트를 생성하고
for n in d:                         # 딕셔너리를 반복해서
    l.append(d[n])                  # 점수만 리스트에 append한 후
l.sort()                            # 오름차순으로 정렬한다
minN = ans                          # 최소점수를 저장할 변수를 생성하고
for n in range(M-K):                # 필수과목을 뺀 수강과목을 반복해서
    minN += l[n]                    # 낮은 점수를 더해준다
print(minN)                         # 받을 수 있는 최소점수를 출력한다
maxN = ans                          # 최대점수를 저장할 변수를 생성하고
for n in range(M-K):                # 필수과목을 뺀 수강과목을 반복해서
    maxN += l[-1-n]                 # 높은 점수를 더해준다
print(maxN)                         # 받을 수 있는 최대 점수를 출력한다