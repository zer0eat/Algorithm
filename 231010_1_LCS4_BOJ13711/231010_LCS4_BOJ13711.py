# LCS4_BOJ13711

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import bisect

# input 받기
N = int(input())                                # 두 수열의 길이를 input 받고
A = list(map(int, input().split()))             # 수열 A를 리스트로 input 받고
B = list(map(int, input().split()))             # 수열 B를 리스트로 input 받는다
tmp = []                                        # 인덱스를 저장할 리스트를 생성하고
for a in A:                                     # 수열 A를 반복해서
    tmp.append(B.index(a))                      # 원소 a가 수열 B에 해당하는 인덱스를 tmp에 append한다
ans = [tmp[0]]                                  # 최장 증가 부분 수열을 구하기 위해 tmp에 첫 원소를 넣고 리스트를 생성하고
for i in range(1, N):                           # tmp에 저장된 A의 B위치를 반복해서
    if ans[-1] < tmp[i]:                        # ans 맨 뒤에 저장된 원소보다 tmp[i]가 더 뒤에 있다면
        ans.append(tmp[i])                      # ans 뒤에 tmp[i]를 append하고
    else:                                       # ans 맨 뒤에 저장된 원소보다 tmp[i]가 더 앞에 있다면
        idx = bisect.bisect_left(ans, tmp[i])   # tmp[i]보다 처음으로 커지는 ans의 원소를 찾아 idx에 저장하고
        ans[idx] = tmp[i]                       # idx 위치에 있는 원소를 tmp[i]로 바꿔준다
print(len(ans))                                 # 두 수열의 LCS의 크기를 출력한다