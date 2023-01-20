# 연속합_BOJ1912

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())               # 수열의 길이를 input 받고
lst = list(map(int, sys.stdin.readline().split()))  # 수열을 list로 input 받는다

for i in range(1, N):                               # 수열의 첫번째 숫자만 빼고 반복해서
    if lst[i-1] > 0:                                # 이전 인덱스까지 계산한 최고 값이 양수라면
        lst[i] = lst[i] + lst[i-1]                  # 이전 인덱스의 요소와 현재 요소를 더한 값이 최대 값이 되므로  두 수를 더한 합을 저장한다
    else:                                           # 이전 인덱스의 합이 음수라면
        pass                                        # 앞의 수를 안 더하는 것이 해당인덱스의 최대 값이 되므로 패스한다

print(max(lst))                                     # 모든 요소 중 최대 값을 출력한다


