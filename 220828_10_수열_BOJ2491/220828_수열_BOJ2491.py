# 수열_BOJ2491

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                # 나오는 수열의 개수
arr = list(map(int, input().split()))   # 수열을 리스트로 input

# 수열 찾기
maxup = 0                       # 오름차순 중 가장 긴 길이를 저장할 변수
maxdown = 0                     # 내림차순 중 가장 긴 길이를 저장할 변수

cnt = 0                         # 길이를 저장할 변수
for a in range(len(arr)-1):     # 수열을 다음 값과 비교하기 위해 처음부터 마지막에서 하나 전 요소까지 반복할 때
    if arr[a] <= arr[a+1]:      # 현재요소보다 다음요소가 같거나 크면
        cnt += 1                # cnt에 1을 추가한다
    elif arr[a] > arr[a+1]:     # 현재요소보다 다음요소가 작다면
        if cnt > maxup:         # maxup보다 cnt가 큰경우엔
            maxup = cnt         # maxup을 cnt로 바꿔주고
            cnt = 0             # cnt 초기화
        else:                   # 그렇지 않다면
            cnt = 0             # cnt만 초기화
else:                           # 반복문이 종료되었을 때
    if cnt > maxup:             # maxup보다 cnt가 크다면
        maxup = cnt             # maxup을 cnt로 바꿔주고
        cnt = 0                 # cnt 초기화

for a in range(len(arr)-1):     # 위와 같은 방법으로 내림차순 중 가장 큰 길이 찾기
    if arr[a] >= arr[a+1]:
        cnt += 1
    elif arr[a] < arr[a+1]:
        if cnt > maxdown:
            maxdown = cnt
            cnt = 0
        else:
            cnt = 0
else:
    if cnt > maxdown:
        maxdown = cnt
        cnt = 0
    else:
        cnt = 0

if maxup >= maxdown:            # 오름차순의 길이가 더 길다면
    print(maxup + 1)            # 오름차순인 원소를 출력(마지막으로 비교한 값을 기준으로 그 다음값도 해당이기에 1을 더해서 출력)
elif maxup < maxdown:           # 내림차순의 길이가 더 길다면
    print(maxdown + 1)          # 내림차순인 원소를 출력