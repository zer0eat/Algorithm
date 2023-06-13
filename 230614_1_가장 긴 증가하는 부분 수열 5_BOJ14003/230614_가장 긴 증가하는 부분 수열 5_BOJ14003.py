# 가장 긴 증가하는 부분 수열 5_BOJ14003

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())                        # 수열의 크기를 input 받고
lst = list(map(int, input().split()))   # 수열을 리스트로 input 받는다
ans = [-1000000001]                     # 가장 긴 증가하는 부분수열을 저장할 리스트를 생성하고 가장 작은값보다 작은 값을 넣어 기준점을 생성한다
visited = [0] * A                       # 현재 수열이 증가하는 수열 중 몇번 째인지 저장할 리스트를 생성한다
cnt = 0                                 # 수열의 인덱스를 저장할 변수 생성
for l in lst:                           # 수열 리스트를 반복해서
    if ans[-1] < l:                     # 현재원소가 ans에 저장된 마지막 값보다 크다면
        visited[cnt] = len(ans)         # visited의 cnt번째 원소에 ans의 길이를 저장해서 현재 수열이 증가하는 수열 중 몇번 째인지 저장한다
        ans.append(l)                   # ans에 append
        cnt += 1                        # 다음 수열의 원소를 표시하기 위해 cnt를 1 추가한다
    else:                               # 현재원소가 ans에 저장된 마지막 값보다 작거나 같다면
        left = 0                        # ans의 왼쪽포인터를 생성하고
        right = len(ans)                # ans의 오른쪽포인터를 생성한다
        while left < right:             # left가 right보다 커질때까지 반복해서
            mid = (left + right) // 2   # mid를 두 포인터의 가운데 정수로 저장한다
            if ans[mid] < l:            # ans[mid]의 값이 현재원소보다 작다면
                left = mid + 1          # 왼쪽 포인터를 mid + 1로 저장한다
            elif ans[mid] > l:          # ans[mid]의 값이 현재원소보다 크다면
                right = mid             # 오른쪽 포인터를 mid로 저장한다
            else:                       # ans[mid]의 값이 현재원소보다 같다면
                right = mid             # 오른쪽 포인터를 mid로 저장하고
                break                   # while문을 break한다
        ans[right] = l                  # ans의 right번째 원소를 현재원소로 바꿔 저장한다
        visited[cnt] = right            # visited의 cnt번째 원소에 right를 저장해서 현재 수열이 증가하는 수열 중 몇번 째인지 저장한다
        cnt += 1                        # 다음 수열의 원소를 표시하기 위해 cnt를 1 추가한다
print(len(ans)-1)                       # 가장 긴 증가하는 부분 수열의 크기를 출력한다

answer = []                             # 가장 긴 증가하는 부분 수열을 저장할 리스트 생성
order = max(visited)                    # 가장 긴 증가하는 부분 수열의 가장 큰 순서를 order에 저장한 후
for i in range(A-1, -1, -1):            # 수열을 역순으로 반복해서
    if visited[i] == order:             # 해당 순서의 원소가 나오면
        answer.append(lst[i])           # answer 리스트에 원소를 append
        order -= 1                      # 순서를 1 감소한다
answer.sort()                           # answer 리스트를 오름차순으로 정렬한 후
print(*answer)                          # 가장 긴 증가하는 부분 수열을 출력한다