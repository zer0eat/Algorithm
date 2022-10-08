# 영화감독숌_BOJ1436

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())   # N 번째 영화 제목

cnt = 0                         # 영화 제목이 가능한 숫자가 나오면 개수를 저장할 변수 생성
n = 665                         # 영화 제목으로 들어갈 숫자를 저장한 변수 생성
while cnt < N:                  # 영화 제목이 가능한 숫자의 개수가 N번째 숫자만큼 도달할때까지 반복
    n += 1                      # 영화 제목을 1 더하고
    a = str(n)                  # 문자열로 바꾸어 a에 저장한 후
    if '666' in a:              # a에 666이 들어있어 영화제목으로 사용이 가능하다면
        cnt += 1                # cnt에 1을 추가하고
else:                           # 반복이 끝났으면 N번째 영화 제목을 출력한다
    print(n)