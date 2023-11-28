# 자전거 묘기_BOJ25706

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 도로의 길이를 input 받고
road = list(map(int, input().split()))  # 점프대의 높이를 리스트로 input 받는다
ans = [0]*N                             # 정답을 저장할 리스트를 생성하고
ans[-1] = 1                             # 마지막 칸을 1로 저장한다
for i in range(N-2,-1,-1):				# N-1칸부터 첫번째 칸까지 반복해서
    if N>i+road[i]+1:					# 현재칸에서 점프대를 뛰었을 때 마지막칸을 넘어가지 않는다면
        ans[i] = ans[i+road[i]+1]+1		# i번째 칸은 점프해서 도착한 곳에서부터 한칸 더 밟게 되므로 해당값을 저장한다
    else:								# 현재칸에서 점프대를 뛰었을 때 마지막칸을 넘어간다면
        ans[i] = 1						# i번째에서 출발했을 때 1칸을 밟는다고 저장한다
print(*ans)                       		# 각 칸에서 자전거를 타고 앞으로 달리면 총 몇 개의 칸을 밟게 되는지 출력한다