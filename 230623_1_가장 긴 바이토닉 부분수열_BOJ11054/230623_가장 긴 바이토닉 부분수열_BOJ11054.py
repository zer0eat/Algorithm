# 가장 긴 바이토닉 부분수열_BOJ11054

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 수열의 크기를 input 받고
lst = list(map(int, input().split()))                           # 수열 리스트를 input 받는다
R_lst = lst[::-1]                                               # 수열 리스트를 뒤집어서 저장한 후
increase = [1] * N                                              # 가장 긴 증가 수열을 저장할 리스트를 생성하고
decrease = [1] * N                                              # 가장 긴 감소 수열을 저장할 리스트를 생성한다

for i in range(N):                                              # 수열의 크기를 반복하고
    for j in range(i):                                          # 해당 수열의 원소까지 반복해서
        if lst[i] > lst[j]:                                     # lst 리스트에서 i번째 수열이 i보다 앞에 있는 원소보다 큰 경우에는
            increase[i] = max(increase[i], increase[j]+1)       # 가장 긴 증가 수열의 i번째 인덱스에 현재 인덱스와 j번째 인덱스에서 1 증가한 수 중 더 큰 수를 저장한다
        if R_lst[i] > R_lst[j]:                                 # R_lst 리스트에서 i번째 수열이 i보다 앞에 있는 원소보다 큰 경우에는
            decrease[i] = max(decrease[i], decrease[j]+1)       # 가장 긴 감소 수열의 i번째 인덱스에 현재 인덱스와 j번째 인덱스에서 1 증가한 수 중 더 큰 수를 저장한다
decrease.reverse()                                              # 모든 수열을 탐색한 후에 가장 긴 감소 수열 리스트를 뒤집는다

ans = 0                                                         # 정답을 저장할 변수를 생성하고
for i in range(N):                                              # 수열의 크기를 반복해서
    tmp = increase[i] + decrease[i]                             # tmp에 i번째 원소가 가장 큰 수일때 가장 긴 바이토닉 수열의 길이를 저장하고
    if ans < tmp:                                               # tmp가 ans보다 크면
        ans = tmp                                               # ans를 tmp로 저장한다

print(ans-1)                                                    # 모든 원소의 탐색을 마친 후 i번째 원소는 증가 수열과 감소 수열 중복으로 카운트 되므로 -1 뺀 후 출력한다