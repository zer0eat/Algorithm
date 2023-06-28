# 로프_BOJ2217

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 로프의 개수
lst = []                        # 로프가 버틸 수 있는 중량을 저장할 리스트 생성
for _ in range(N):              # 로프의 수를 반복해서
    lst.append(int(input()))    # 로프별 버틸수 있는 중량을 lst에 append
lst.sort()                      # lst를 오름차순으로 정렬하고
ans = 0                         # 최대 중량을 저장할 변수 생성
for i in range(N):              # 로프의 수를 반복해서
    if ans < lst[i] * (N - i):  # 버틸 수 있는 중량을 하나씩 빼면서 최대중량을 비교할 때 더 많은 무게를 버틸 수 있는 조합이 나왔다면
        ans = lst[i] * (N - i)  # ans를 최대중량으로 갱신한다
print(ans)                      # 모든 탐색을 마친 후 최대 중량을 출력한다