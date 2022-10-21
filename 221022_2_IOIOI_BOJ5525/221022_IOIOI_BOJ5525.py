# IOIOI_BOJ5525

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())               # N = I와 O의 개수를 결정할 정수
M = int(sys.stdin.readline())               # M = 주어진 문자열의 길이
ans = sys.stdin.readline().rstrip()         # ans = 주어진 문자열

n = 1                                       # 인덱스로 사용할 n을 1로 생성
cnt = 0                                     # ans 안에 있는 N개의 IOI의 수
tmp = 0                                     # IOI의 수
while n < (M - 1):                          # 인덱스가 M-1보다 작으면 반복해서
    if ans[n-1] == 'I'and ans[n] == 'O' and ans[n+1] == 'I':    # 현재 인덱스가 O이고 앞뒤로 I라면
        tmp += 1                            # IOI의 숫자를 1 올리고
        if tmp >= N:                        # IOI의 숫자가 N개를 넘어섰다면
            cnt += 1                        # cnt를 1 추가한다
        n += 2                              # 인덱스를 2칸 이동한다
    else:                                   # 만약 충족하지 않는다면
        n += 1                              # 인덱스를 1칸 이동하고
        tmp = 0                             # tmp를 초기화 한다

print(cnt)                                  # cnt의 개수를 출력한다
