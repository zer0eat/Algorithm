# 보석도둑_BOJ1202

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# input 받기
N, K = map(int, sys.stdin.readline().split())                   # N 보석의 개수 / K 가방의 개수

jewerly = []                                                    # 보석을 저장할 리스트를 만들고
for _ in range(N):                                              # 보석의 수 만큼 반복해서
    M, V = map(int, sys.stdin.readline().split())               # M 보석의 무게 / V 보석의 가치
    heappush(jewerly, (M, -V))                                  # jewerly 리스트에 무게의 최소힙 / -가치의 최소힙(가치의 최대힙으로 구하기 위해)으로 heappush한다

bag = [int(sys.stdin.readline().strip()) for _ in range(K)]     # 가방의 크기를 리스트로 input 받고
bag.sort()                                                      # 오름차순으로 정렬한다

ans = 0                                                         # 훔칠 보석의 총 가치를 저장할 변수를 생성하고
tmp = []                                                        # 훔칠 보석의 가치를 저장할 리스트를 생성한다
for b in bag:                                                   # 가방을 반복해서
    while jewerly and b >= jewerly[0][0]:                       # 훔칠 수 있는 보석이 남아있고, 가방의 크기보다 보석의 무게가 같거나 작다면
        heappush(tmp, heappop(jewerly)[1])                      # 보석의 가치를 tmp에 저장한다
    if tmp:                                                     # tmp에 훔칠 보석이 들어있다면
        ans -= heappop(tmp)                                     # heappop해서 가치를 ans에 더해준다
    elif not jewerly:                                           # 더이상 훔칠 보석이 남아있지 않다면
        break                                                   # for문을 break한다
print(ans)                                                      # 훔칠 보석의 가치를 출력한다