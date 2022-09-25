# 트리의부모찾기_BOJ11725

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                            # 노드의 개수
tree = [[] for _ in range(N+1)]             # 트리의 연결을 저장할 리스트 생성
for n in range(N-1):                        # input을 받기위해 연결된 선의 수만큼 반복할 때
    a, b = map(int, input().split())        # 선으로 연결된 양 끝의 노드를 a,b에 저장하고
    tree[a].append(b)                       # 인덱스가 a일 때 b를 append
    tree[b].append(a)                       # 인덱스가 b일 때 a를 append

q = []                                      # q를 생성하고
ans = dict()                                # 정답을 저장할 딕셔너리를 생성한다
for u in tree[1]:                           # 뿌리가 되는 노드인 1을 반복해서
    q.append(u)                             # q에 연결된 노드를 쌓고
    ans[u] = 1                              # 딕셔너리에 자식노드가 key이고 부모노드가 value가 되도록 저장한다
tree[1] = []                                # 반복이 끝났으면 탐색한 리스트는 비워준다

while q:                                    # q가 빌때까지 반복할 때
    a = q.pop(0)                            # q의 맨앞의 요소를 빼서 a에 저장한 후
    for o in tree[a]:                       # a인덱스의 트리리스트를 반복해서
        if tree[o] != []:                   # 비어있지 않은 경우에만
            q.append(o)                     # 새로운 요소를 q에 append 하고
            ans[o] = a                      # ans 딕셔너리에 자식노드가 key이고 부모노드가 value가 되도록 저장한다
    else:                                   # 반복이 끝났으면 탐색한 리스트는 비워준다
        tree[a] = []

for n in range(2, N+1):                     # 2번부터 마지막까지 반복해서
    print(ans[n])                           # value를 출력한다

