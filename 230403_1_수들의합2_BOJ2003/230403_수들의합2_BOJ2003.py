# 수들의합2_BOJ2003

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 수열을 수 / M 연속하는 수열의 합
lst = list(map(int, input().split()))   # 수열을 리스트형태로 input 받음

A = 0                                   # 시작값을 가르키는 포인터
B = 0                                   # 마지막값을 가르키는 포인터

ans = 0                                 # A부터 B까지의 합이 M이 되는 수를 저장할 변수 생성
while B < N:                            # B가 N보다 작을 때 반복해서
    if sum(lst[A:B+1]) == M:            # A부터 B까지의 합이 M이라면
        ans += 1                        # ans에 1을 더하고
        B += 1                          # B를 오른쪽으로 한칸 이동시킨다
    elif sum(lst[A:B+1]) > M:           # A부터 B까지의 합이 M보다 크다면
        A += 1                          # A를 오른쪽으로 한칸 이동시킨다
    else:                               # A부터 B까지의 합이 M보다 작다면
        B += 1                          # B를 오른쪽으로 한칸 이동시킨다
print(ans)                              # while을 마쳤다면 ans를 출력한다