# 내 뒤에 나와 다른 수_BOJ24523

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 수열의 길이를 input 받고
lst = list(map(int, input().split()))   # 수열을 리스트로 input 받는다
ans = [-1]*N                            # 정답을 저장할 리스트를 생성하고
now = lst[0]                            # 현재 원소를 저장할 변수를 생성하고
tmp = []                                # now와 같은 원소를 저장할 리스트를 생성한다
for i in range(N):                      # 수열을 반복해서
    if lst[i] == now:                   # i번째 원소가 now와 같은 원소라면
        tmp.append(i)                   # tmp에 i인덱스를 append한다
    else:                               # i번째 원소와 now가 다르다면
        for t in tmp:                   # tmp를 반복해서
            ans[t] = i+1                # 포함된 인덱스의 순번을 i+1로 저장한다
        else:                           # tmp를 모두 반복했다면
            now = lst[i]                # now를 i번째 원소로 저장하고
            tmp = [i]                   # tmp에 i를 넣어 리스트를 생성한다
print(*ans)                             # 내 뒤에 나와 다른 수가 나오는 순번을 출력한다