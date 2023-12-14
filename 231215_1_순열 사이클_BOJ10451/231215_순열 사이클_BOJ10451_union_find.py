# 순열 사이클_BOJ10451

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def find(N):
    if parent[N] != N:                      # N과 부모 원소가 다르다면
        parent[N] = find(parent[N])         # find 함수로 N의 부모원소를 탐색한다
    return parent[N]                        # N과 부모원소가 같아진 값을 return한다

def union(x, y):
    root_x = find(x)                        # x의 부모 원소를 찾아 저장하고
    root_y = find(y)                        # y의 부모 원소를 찾아 저장한 후
    if root_x > root_y:                     # root_y가 더 작다면
        parent[root_x] = root_y             # root_x의 부모를 root_y로 저장한고
    else:                                   # root_x가 더 작다면
        parent[root_y] = root_x             # root_y의 부모를 root_x로 저장한다

T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N = int(input())                        # 순열의 크기를 input 받고
    lst = list(map(int, input().split()))   # 순열을 input받는다
    parent = dict()                         # 부모를 저장할 딕셔너리를 생성하고
    for i in range(N):                      # 순열의 원소를 반복해서
        parent[i] = i                       # i의 부모를 i로 저장한다
    for i in range(N):                      # 순열의 원소를 반복해서
        union(i, lst[i] - 1)                # i와 연결된 원소를 union 함수로 결합한다
    ans = set()                             # 정답을 저장할 set을 생성하고
    for i in range(N):                      # 순열의 원소를 반복해서
        ans.add(find(i))                    # i의 부모 원소를 ans에 add하고
    print(len(ans))                         # 부모 원소의 개수를 구해서 사이클의 수를 출력한다