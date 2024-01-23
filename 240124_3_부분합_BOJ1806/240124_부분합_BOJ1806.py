# 부분합_BOJ1806

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, S = map(int, input().split())        # N 수열의 길이 / S 수열의 최소합을 input 받고
lst = list(map(int, input().split()))   # 수열을 리스트로 input 받는다
ans = 1e9                               # 정답을 저장할 변수를 생성하고
l = 0                                   # 왼쪽을 가르킬 포인터를 생성하고
r = 0                                   # 오른쪽을 가르킬 포인터를 생성한다
tmp = lst[0]                            # 첫번째 원소를 tmp로 저장하고
if tmp >= S:                            # 첫번째 원소가 S를 만족했다면
    print(1)                            # 1을 출력하고
    quit()                              # 종료한다
while l < N:                            # 왼쪽 포인터가 끝까지 마지막 원소를 가르킬때까지 반복해서
    if tmp < S and r < N-1:             # tmp가 S보다 작고 오른쪽 포인터가 끝을 가르키고 있지 않다면
        r += 1                          # 오른쪽 포인터를 한칸 움직이고
        tmp += lst[r]                   # 오른쪽 포인터가 가르키는 원소를 tmp에 추가한다
    else:                               # tmp가 S보다 같거나 크거나 오른쪽 포인터가 끝을 가르킨다면
        tmp -= lst[l]                   # 왼쪽 포인터가 가르키는 원소를 tmp에서 빼주고
        l += 1                          # 왼쪽 포인터를 한칸 이동한다
    if tmp >= S:                        # tmp가 S보다 같거나 큰 조건을 만족한다면
        ans = min(ans, r-l+1)           # ans와 현재 길이 중 더 짧은 값을 저장한다
if ans == 1e9:                          # 합을 만드는 것이 불가능해서 ans가 변하지 않았다면
    print(0)                            # 0을 출력하고
else:                                   # 합이 만드는 경우가 있다면
    print(ans)                          # 최소의 길이를 출력한다