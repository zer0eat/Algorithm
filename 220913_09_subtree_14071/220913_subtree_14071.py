# subtree_14071

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 전위 순회를 위한 함수
def pre(A):
    global ans
    if A:
        ans.append(A)                               # 나를 ans에 append 하고
        pre(ch1[A])                                 # 왼쪽 자식을 탐색하고
        pre(ch2[A])                                 # 오른쪽 자식을 탐색한다

# input 받기
T = int(input())                                    # 테스트케이스
for t in range(T):                                  # 테스트케이스를 반복할 때
    E, N = map(int, input().split())                # E는 노드 쌍의 개수 / N 출발 노드의 번호
    node = list(map(int, input().split()))          # 노드 쌍을 리스트로 input 받음

    ch1 = [0]*(E+2)                                 # 왼쪽 자식의 인덱스를 저장할 리스트를 만들고
    ch2 = [0]*(E+2)                                 # 오른쪽 자식의 인덱스를 저장할 리스트를 만든다
    ans = []                                        # 전위 순회를 했을 때 순서를 저장할 리스트를 만들고

    for e in range(E):                              # 노드 쌍을 반복할 때
        if ch1[node[2 * e]] != 0:                   # 한 노드에서 분기된 노드가 있다면
            ch2[node[2 * e]] = node[2 * e + 1]      # ch2에 저장하고
        else:                                       # 한 노드에서 분기된 노드가 없다면
            ch1[node[2 * e]] = node[2 * e + 1]      # ch1에 저장한다
    else:                                           # 반복이 끝나면
        pre(N)                                      # N번 노드부터 전위 순회를 했을 때

        print(f'#{t+1}', len(ans))                  # 지나가는 노드의 개수를 출력한다





