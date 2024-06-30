# 임시 반장 정하기_BOJ1268

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 학생의 수를 input 받고
ban = [list(map(int, input().split())) for _ in range(N)]   # 학생별로 1부터 5학년 동안 반을 input 받고
cnt, ans = 0, 1                                             # 다른 친구들과 가장 많이 같은 반이 된 횟수와 학생의 번호를 생성하고
for n in range(N):                                          # 기준 학생을 반복하고
    tmp = [0]*N                                             # 같은 반을 표시할 리스트를 생성하고
    for m in range(5):                                      # 1부터 5학년까지 반복하고
        for k in range(N):                                  # 비교 학생을 반복해서
            if n != k:                                      # 같은 학생이 아니라면
               if ban[n][m] == ban[k][m]:                   # n과 k 학생이 같은 m 학년에 같은 반이었다면
                   tmp[k] = 1                               # k학생을 같은반 표시한다
    else:                                                   # 모든 학생의 반을 확인하고
        if cnt < sum(tmp):                                  # n번째 학생이 다른 학생과 가장 많이 같은 반이 되었다면
            cnt = sum(tmp)                                  # 같은 반이 된 수를 cnt에 저장하고
            ans = n+1                                       # 임시 반장이 될 n번째 학생의 번호를 저장한다
print(ans)                                                  # 임시 반장의 번호를 출력한다