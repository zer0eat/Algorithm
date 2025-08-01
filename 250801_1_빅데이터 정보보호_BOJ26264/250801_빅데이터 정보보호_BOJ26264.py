# 빅데이터 정보보호_BOJ26264

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
b, s = 0, 0                     # 관심사를 저장할 변수를 생성하고
N = int(input())                # 학생의 수를 input받는다
idx, tmp = 0, 0                 # 인덱스와 관심사의 수를 저장할 변수를 생성하고
S = list(input().strip())       # 관심사를 리스트로 input받는다
while tmp < N:                  # 관심사의 수를 모두 확인할 때까지 반복해서
    if S[idx] == 'b':           # 관심사가 빅데이터라면
        b += 1                  # 빅데이터를 1 추가하고
        tmp += 1                # 관심사를 1 추가하고
        idx += 7                # 다음 관심사로 인덱스를 옮겨준다
    else:                       # 관심사가 시큐리티라면
        s += 1                  # 시큐리티를 1 추가하고
        tmp += 1                # 관심사를 1 추가하고
        idx += 8                # 다음 관심사로 인덱스를 옮겨준다
if b > s:                       # 빅데이터가 더 관심이 많다면
    print('bigdata?')           # 빅데이터를 출력하고
elif b < s:                     # 시큐리티가 더 관심이 많다면
    print('security!')          # 시큐리티를 출력하고
else:                           # 관심이 같다면
    print('bigdata? security!') # 둘 다 출력한다