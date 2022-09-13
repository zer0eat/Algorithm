#_이진탐색_14073

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 중위 순회
def inorder(A):
    global tree
    if A:
        inorder(ch1[A])                 # 왼쪽 자식을 탐색
        tree.append(A)                  # 나를 tree에 append
        inorder(ch2[A])                 # 오른쪽 자식을 탐색

# input 받기
T = int(input())                        # 테스트 케이스
for t in range(T):                      # 테스트 케이스 반복
    N = int(input())                    # 노드의 개수

    ans = [0] * (N + 1)                 # 노드를 인덱스로 리스트 생성
    tree = []                           # 중위탐색 순서를 저장할 빈리스트
    ch1 = [0] * (N + 1)                 # 왼쪽 자식 인덱스를 저장할 리스트
    ch2 = [0] * (N + 1)                 # 오른쪽 자식 인덱스를 저장할 리스트

    for n in range(1, N + 1):           # 1번 부터 반복하면서
        if 2 * n <= N:                  # N노드 보다 자식노드가 작다면
            ch1[n] = 2 * n              # ch1에 연결된 자식 노드 인덱스를 요소로 저장
        if 2 * n + 1 <= N:              # N노드 보다 자식노드가 작다면
            ch2[n] = 2 * n + 1          # ch2에 연결된 자식 노드 인덱스를 요소로 저장

    inorder(1)                          # 중위 순회를 한 후

    q = 1                               # 각 노드에 부여할 값을 변수로 만든 후
    for e in tree:                      # 중위 순회한 순서대로
        ans[e] = q                      # 순서에 맞게 q값을 부여하고 
        q += 1                          # q를 1 증가시킨다

    print(f'#{t+1}', ans[1], ans[N//2])

