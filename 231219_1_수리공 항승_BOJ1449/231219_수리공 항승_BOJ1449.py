# 수리공 항승_BOJ1449

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, L = map(int, input().split())        # N 구멍난 부분의 수 / L 테이프의 길이 를 input 받고
pipe = list(map(int, input().split()))  # 구멍난 부분의 위치를 input 받는다
pipe.sort()                             # 구멍난 부분을 오름차순으로 정렬하고
ans = 0                                 # 필요한 테이프의 수를 저장할 변수를 생성한다
visited = [0] * 1001                    # 테이프를 붙인 부분을 표시할 리스트를 생성하고
for p in pipe:                          # 구멍난 부분을 반복해서
    if visited[p] == 0:                 # 구멍난 부분에 테이프가 붙어있지 않다면
        ans += 1                        # 테이프의 수를 1 추가하고
        for i in range(L):              # 테이프를 붙인 부분부터 L만큼 반복해서
            if p+i < 1001:              # 테이프를 붙일 부분이 전체 길이보다 짧다면
                visited[p+i] = 1        # 해당 위치에 테이프를 붙였다는 표시를 해준다
print(ans)                              # 모든 구멍을 막았다면 필요한 테이프의 개수를 출력한다