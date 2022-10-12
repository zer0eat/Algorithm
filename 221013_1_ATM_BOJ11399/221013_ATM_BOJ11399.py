# ATM_BOJ11399

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                       # 사람의 수
arr = list(map(int, sys.stdin.readline().split()))  # 사람마다 인출하는데 걸리는 시간

arr.sort()                                          # 오름차순으로 정렬

for n in range(1, N):                               # 1번 인덱스부터 반복해서
    arr[n] = arr[n] + arr[n-1]                      # 걸리는 시간을 인출하는데 걸리는 시간 + 이전 사람들이 걸리는 시간으로 변경

print(sum(arr))                                     # 총 소모시간의 합을 출력