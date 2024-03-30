# 꿍의 우주여행_BOJ9501

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N, D = map(int, input().split())        # N 우주선의 수 / D 도달 거리를 input 받고
    ans = 0                                 # 정답을 저장할 변수를 생성하고
    for n in range(N):                      # 우주선의 수를 반복해서
        v, f, c = map(int, input().split()) # v 우주선의 속도 / f 우주선의 연료 / c 우주선의 연비를 input 받고
        if v * f / c >= D:                  # 가지고 있는 연료로 목적지를 갈 수 있다면
            ans += 1                        # 정답에 도착 가능한 우주선을 1 추가한다
    print(ans)                              # 목적지까지 갈 수 있는 우주선의 개수를 출력한다