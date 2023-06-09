# 가장 긴 증가하는 부분 수열 2_BOJ12015

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())                        # 수열의 크기
lst = list(map(int, input().split()))   # 수열을 리스트로 input
ans = [0]                               # 가장 긴 증가하는 부분 수열을 저장할 리스트 생성

for l in lst:                           # 수열을 반복해서
    if ans[-1] < l:                     # 수열의 원소가 ans의 마지막 값보다 크다면
        ans.append(l)                   # ans에 append
    else:                               # 수열의 원소가 ans의 마지막 값보다 작다면
        left = 0                        # 이분탐색의 왼쪽 원소 포인터로 사용할 변수 생성
        right = len(ans)                # 이분탐색의 오른쪽 원소 포인터로 사용할 변수 생성
        while left < right:             # 왼쪽 포인터가 오른쪽 포인터보다 커질때까지 반복해서
            mid = (right + left) // 2   # 두 포인트의 중간값을 찾는다
            if ans[mid] < l:            # 중간값이 l보다 작다면
                left = mid + 1          # left를 중간값 +1로 변경
            elif ans[mid] > l:          # 중간값이 l보다 크다면
                right = mid             # right를 중간값으로 변경
            else:                       # 중간값이 l보다 같다면
                right = mid             # right를 중간값으로 변경
                break                   # while문을 break
        ans[right] = l                  # 반복을 마쳤다면 오른쪽 포인터가 가르키는 원소를 l로 바꾼다
print(len(ans)-1)                       # 가장 긴 증가하는 부분 수열의 크기를 출력한다