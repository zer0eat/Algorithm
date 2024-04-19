# 진법변환 2_BOJ11005

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, B = map(int, input().split())    # N 10진법의 수 / B 진법을 input 받고
ans = ''                            # 정답을 저장할 변수를 생성하고
A = 1                               # N을 나눠줄 변수를 생성한다
while 1:                            # break가 나올때까지 반복해서
    if N >= A*B:                    # 진법을 한자리 올렸을 때 N보다 작으면
        A *= B                      # A에 B를 곱해 진법을 하나 올리고
    else:                           # N이 더 작다면
        break                       # while문을 종료한다
while A > 0:                        # A가 0이 될때까지 반복해서
    if N//A > 9:                    # N을 A진법으로 변환했을 때 10 이상이라면
        ans += str(chr(N//A+55))    # 정답에 N을 B진법으로 전환한 문자를 더해주고
    else:                           # N을 A진법으로 변환했을 때 10보다 작다면
        ans += str(N//A)            # 정답에 N을 B진법으로 전환한 수를 더해주고
    N %= A                          # N을 A로 나눈 나머지로 저장하고
    A //= B                         # A를 B로 나눠준다
print(ans)                          # 10진법 수 N을 B진법으로 출력한다