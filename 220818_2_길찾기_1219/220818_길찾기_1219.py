# 길찾기_1219

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 방문 함수 만들기
def node(start):                                # node 함수에 시작점을 입력했을 때
    visited[start] = 1                          # 시작점을 방문 지도에 1로 표시하고
    for x in load[start]:                       # start 지점에서 갈 수 있는 곳을 반복문으로 돌렸을 때
        if visited[x] == 0:                     # 갈 수 있는 곳이 아직 방문 전이면
            node(x)                             # 그 지점을 시작점으로 다시 함수를 돌린다

# input 받기
T = 10                                          # 테스트 케이스가 10개 일 때
for t in range(T):                              # 테스트 케이스만큼 반복문을 돌린다
    case, length = map(int, input().split())    # 테스트 케이스 번호와 순서쌍의 수를 입력 받는다
    lst = list(map(int, input().split()))       # 순서쌍을 리스트 lst로 입력 받는다.

    load = [[] for _ in range(100)]             # 각 분기점의 수만큼 빈 리스트를 만들어준다

    for l in range(len(lst)):                   # 순서쌍이 담긴 리스트를 반복할 때
        if l % 2 == 0:                          # 짝수의 인덱스를 같는 요소가 나왔을 때
            load[lst[l]].append(lst[l+1])       # load의 lst[l]번째 리스트에 lst[l+1]를 추가한다

    visited = [0] * 100                         # 방문지점을 알아보기 위한 빈 지도를 리스트로 만든 후
    start = 0                                   # 시작지점 A를 0으로
    end = 99                                    # 끝나는지점 B를 99로 입력한후

    node(start)                                 # 방문 함수를 돌린후

    print(f'#{case}', visited[99])              # start에서 시작했을때 end까지 방문했는지 출력한다