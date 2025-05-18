# 진수 변환기_BOJ14915

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
M, N = map(int, input().split())    # 변환할 수와 변환할 진수를 input받고
ans = ''                            # 정답을 저장할 변수를 생성해서
dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}  # 변환할 수와 대응하는 딕셔너리를 생성하고
if M == 0:                          # 변환할 수가 0이라면
    ans = '0'                       # 변환된 수를 0으로 출력한다
while M > 0:                        # 변환할 수가 0이 될때까지 반복해서
    tmp = M % N                     # 변환할 수를 N진수로 변경하고
    if tmp >= 10:                   # 변환할 수가 10이상이라면
        tmp = dic[tmp]              # 수를 알파벳으로 변환하고
    ans = str(tmp) + ans            # N진수를 변환해서 저장하고
    M //= N                         # 변환할 수를 진수변환하고 남은 수를 저장하고
print(ans)                          # N진수로 변환된 수를 출력한다