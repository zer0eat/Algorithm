# 트럭_BOJ13335

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input.txt 열기
N, W, L = map(int, input().split())     # N 트럭의 수 / W 다리의 길이 / L 다리의 하중을 input 받고
truck = list(map(int, input().split())) # 트럭의 하중을 리스트로 input 받고
bridge = deque([0]*W)                   # 다리를 지나가는 트럭을 구현하기 위한 deque를 생성하고
time = 0                                # 트럭이 지나갈 때 드는 시간을 저장할 변수를 생성하고
idx = 0                                 # 다리에 입장할 트럭을 가르키는 포인터를 생성한 후
while idx < N:                          # 포인터가 마지막 트럭을 가르킬 때까지 반복해서
    bridge.popleft()                    # 다리의 맨 앞에 있는 트럭이 빠지고
    time += 1                           # 시간을 1 추가한다
    if sum(bridge) + truck[idx] <= L:   # 다리위의 트럭의 무게와 다음 입장할 트럭의 무게의 합이 L보다 작거나 같다면
        bridge.append(truck[idx])       # 다리에 트럭을 올리고
        idx += 1                        # 포인터를 한칸 이동한다
    else:                               # 다리위의 트럭의 무게와 다음 입장할 트럭의 무게의 합이 L보다 크다면
        bridge.append(0)                # 트럭이 다리를 지나갈 수 없으므로 0을 올린다
print(time+W)                           # 마지막 트럭까지 다리에 올라간 시간과 다리의 길이만큼 더해 트럭들이 다리를 건너는 최단시간을 출력한다