# 수 이어 쓰기 1_BOJ1748

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 이어쓰기할 숫자의 개수를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
length = str(N)                         # input 받은 숫자의 길이를 저장한 변수를 생성하고
for i in range(len(length)):            # 숫자의 길이만큼 반복한다
    if len(length)-1 == i:              # 숫자의 최대길이에 도달하면
        ans += (N-(10**i)+1) * (i+1)    # N에서 최대길이 이전의 수만큼 뺀 후 최대 길이를 곱한 자리수를 ans에 더하고
    else:                               # 숫자의 최대길이가 아니라면
        ans += 9*(10**i) * (i+1)        # 해당 자리수까지의 길이를 더한다
print(ans)                              # 새로운 수의 자릿수를 출력한다