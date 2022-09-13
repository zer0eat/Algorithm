# 중위순회_1231

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 중위 순회를 위한 함수
def inorder(A):
    global ans
    if A:
        inorder(ch1[A])                                 # 왼쪽 자식을 탐색하고
        ans.append(A)                                   # 나를 ans에 append하고
        inorder(ch2[A])                                 # 오른쪽 자식을 탐색한다

# input 받기
T = 10                                                  # 테스트 케이스
for t in range(T):                                      # 테스트 케이스를 반복할 때
    N = int(input())                                    # N에 트리의 노드의 수를 input 받고
    ch1 = [0]*(N+1)                                     # 왼쪽 자식의 인덱스를 저장할 리스트를 만들고
    ch2 = [0]*(N+1)                                     # 오른쪽 자식의 인덱스를 저장할 리스트를 만든다
    word = [[] for _ in range(N+1)]                     # 해당 인덱스의 알파벳을 저장할 리스트를 만든다
    ans = []                                            # 중위 순회를 했을 때 순서를 저장할 리스트를 만들고
    answord = ''                                        # 중위 순회 순서대로 알파벳을 저장할 변수를 만든다

    for n in range(N):                                  # 노드의 숫자만큼 반복 했을 때
        node = list(input().split())                    # 노드의 정보(0:부모노드/1:알파벳/2:왼쪽자식노드/3:오른쪽자식노드) input 받은 후
        word[int(node[0])].append(node[1])              # word 리스트의 부모노드 인덱스에 알파벳을 입력하고
        try:                                            # 시도할 수 있다면
            ch1[int(node[0])] = int(node[2])            # ch1 리스트의 부모노드 인덱스에 왼쪽자식노드 인덱스를 입력하고
        except:                                         # 시도할 수 없다면 패스한다
            pass
        try:                                            # 시도할 수 있다면
            ch2[int(node[0])] = int(node[3])            # ch2 리스트의 부모노드 인덱스에 오른쪽자식노드 인덱스를 입력하고
        except:                                         # 시도할 수 없다면 패스한다
            pass

    inorder(1)                                          # root를 기준으로 중위순회를 한후

    for a in ans:                                       # 나온 순서를 반복해서
        answord += word[a][0]                           # answord에 해당 알파벳을 저장한다

    print(f'#{t+1}', answord)                           # 중위순회 순서대로 나온 알파벳을 출력한다