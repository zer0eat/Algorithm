# 물통_BOJ2251

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C = map(int, input().split())                 # 물통의 부피를 input 받고
visited = dict()                                    # 방문기록을 표시할 딕셔너리를 생성하고
ans = set()                                         # A가 비어있을 때 C의 물의 양을 저장할 set을 생성한다

def bfs(a, b, c):
    if a == 0:                                      # A의 물통이 0일 때
        ans.add(c)                                  # C의 물의 양을 ans에 더하고
    # A->B
    water = min(a, B-b)                             # A의 물의 양을 B로 옮길 때 a의 양과 B 물통의 남은 양 중 적은 양을 water에 저장하고
    if visited.get((a-water, b+water, c)) == None:  # a의 물을 B에 옮긴 후 결과가 방문 전이라면
        visited[(a-water, b+water, c)] = 1          # 방문표시를 하고
        bfs(a-water, b+water, c)                    # 남은 물의 양을 bfs탐색한다
    # A->C
    water = min(a, C-c)                             # A의 물의 양을 C로 옮길 때 a의 양과 C 물통의 남은 양 중 적은 양을 water에 저장하고
    if visited.get((a-water, b, c+water)) == None:  # a의 물을 C에 옮긴 후 결과가 방문 전이라면
        visited[(a-water, b, c+water)] = 1          # 방문표시를 하고
        bfs(a-water, b, c+water)                    # 남은 물의 양을 bfs탐색한다
    # B->A
    water = min(A-a, b)                             # B의 물의 양을 A로 옮길 때 b의 양과 A 물통의 남은 양 중 적은 양을 water에 저장하고
    if visited.get((a+water, b-water, c)) == None:  # b의 물을 A에 옮긴 후 결과가 방문 전이라면
        visited[(a+water, b-water, c)] = 1          # 방문표시를 하고
        bfs(a+water, b-water, c)                    # 남은 물의 양을 bfs탐색한다
    # B->C
    water = min(b, C-c)                             # B의 물의 양을 C로 옮길 때 b의 양과 C 물통의 남은 양 중 적은 양을 water에 저장하고
    if visited.get((a, b-water, c+water)) == None:  # b의 물을 C에 옮긴 후 결과가 방문 전이라면
        visited[(a, b-water, c+water)] = 1          # 방문표시를 하고
        bfs(a, b-water, c+water)                    # 남은 물의 양을 bfs탐색한다
    # C->A
    water = min(A-a, c)                             # C의 물의 양을 A로 옮길 때 c의 양과 A 물통의 남은 양 중 적은 양을 water에 저장하고
    if visited.get((a+water, b, c-water)) == None:  # c의 물을 A에 옮긴 후 결과가 방문 전이라면
        visited[(a+water, b, c-water)] = 1          # 방문표시를 하고
        bfs(a+water, b, c-water)                    # 남은 물의 양을 bfs탐색한다
    # C->B
    water = min(B-b, c)                             # C의 물의 양을 B로 옮길 때 c의 양과 B 물통의 남은 양 중 적은 양을 water에 저장하고
    if visited.get((a, b+water, c-water)) == None:  # c의 물을 B에 옮긴 후 결과가 방문 전이라면
        visited[(a, b+water, c-water)] = 1          # 방문표시를 하고
        bfs(a, b+water, c-water)                    # 남은 물의 양을 bfs탐색한다

bfs(0, 0, C)                                        # 초기 물의 양을 넣고 bfs 탐색해서
ans = sorted(list(ans))                             # C에 담긴 물의 양을 오름차순으로 정렬한 후
print(*ans)                                         # A가 0일 때 C의 물의 양을 출력한다