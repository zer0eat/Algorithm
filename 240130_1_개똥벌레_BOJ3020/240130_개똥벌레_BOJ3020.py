# 개똥벌레_BOJ3020

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, H = map(int, input().split())    # N 동굴의 가로길이 / H 동굴의 세로길이를 input받고
up = [0]*H                          # 종유석의 수를 저장할 리스트를 생성하고
down = [0]*H                        # 석순의 수를 저장할 리스트를 생성한다
for i in range(N):                  # 동굴의 길이를 반복해서
    h = int(input())                # 석순 또는 종유석의 길이를 input 받고
    if i%2:                         # 홀수번째라면
        up[H-h] += 1                # 종유석의 최저 높이를 추가하고
    else:                           # 짝수번째라면
        down[h-1] += 1              # 석순의 최고 높이를 추가한다
crush = [0]*H                       # 부숴야하는 수를 저장할 리스트를 생성하고
for i in range(H-2, -1, -1):        # 천장보다 한칸 낮은 수부터 0까지 반복해서
    down[i] += down[i+1]            # 한칸 위에 있는 석순만큼 아래에도 있어야하므로 i+1번째 수를 i번째에 더한다
    up[H-i-1] += up[H-i-2]          # 한칸 아래에 있는 종유석만큼 위에도 있어야하므로 H-i-2번째 수를 H-i-1에 더한다
    crush[i] += down[i]             # 석순의 수를 crush에 더하고
    crush[H-i-1] += up[H-i-1]       # 종유석의 수를 crush에 더한다
crush.sort()                        # crush를 오름차순으로 정렬하고
ans = crush[0]                      # ans에 가장 낮은 값을 저장한 변수를 생성하고
num = 1                             # 개수를 1로 저장한 변수를 생성한다
for i in range(1, H):               # 1부터 마지막까지 반복해서
    if ans == crush[i]:             # i번째 수가 최소값과 같다면
        num += 1                    # 개수를 1 더해주고
    else:                           # 다르다면
        break                       # for문을 break한 후
print(ans, num)                     #  파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 출력한다