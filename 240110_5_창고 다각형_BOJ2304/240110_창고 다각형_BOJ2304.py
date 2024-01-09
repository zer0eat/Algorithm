# 창고 다각형_BOJ2304

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 기둥의 개수를 input 받고
end = 0                                 # 마지막 기둥의 위치를 저장할 변수를 생성하고
height = 0                              # 가장 높은 기둥의 높이를 저장할 변수를 생성하고
h_v = 0                                 # 가장 높은 기둥의 위치를 저장할 변수를 생성한다
visited = [0]*1001                      # 기둥의 높이를 저장할 리스트를 생성하고
for n in range(N):                      # 기둥의 개수를 반복해서
    L, H = map(int, input().split())    # L 기둥의 위치 / H 기둥의 높이를 input 받고
    visited[L] = H                      # 기둥의 위치에 높이를 저장해준다
    end = max(end, L)                   # 마지막 기둥의 위치와 현재 기둥의 위치 중 더 뒤에 있는 값을 저장하고
    if height <= H:                     # 현재 저장된 가장 높은 기둥보다 현재 기둥이 더 높다면
       height = H                       # 가장 높은 기둥의 값을 갱신하고
       h_v = L                          # 가장 높은 기둥으 위치를 갱신한다
ans = 0                                 # 창고 다각형의 면적을 저장할 변수를 생성하고
tmp = 0                                 # 현재 기둥의 높이를 저장할 변수를 생성한 후
for i in range(h_v+1):                  # 가장 높은 기둥까지 반복해서
    tmp = max(tmp, visited[i])          # 현재 기둥의 높이와 저장된 높이 중 더 큰 값을 저장하고
    ans += tmp                          # 창고의 면적에 저장된 기둥의 높이를 더한다
tmp = 0                                 # 현재 기둥의 높이를 저장할 변수를 초기화하고
for i in range(end, h_v, -1):           # 뒤에서부터 가장 높은 기둥까지 반복해서
    tmp = max(tmp, visited[i])          # 현재 기둥의 높이와 저장된 높이 중 더 큰 값을 저장하고
    ans += tmp                          # 창고의 면적에 저장된 기둥의 높이를 더한다
print(ans)                              # 가장 작은 창고 다각형의 면적을 출력한다