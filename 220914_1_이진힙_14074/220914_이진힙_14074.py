# 이진힙_14074

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스를 반복할 때
    N = int(input())                                                # 노드의 개수를 받음
    arr = list(map(int, input().split()))                           # 노드의 값을 리스트로 받음
    tree = [0]                                                      # heap으로 정렬할 리스트를 생성하고

    for n in range(N):                                              # 노드의 수만큼 반복하면서
        tree.append(arr[n])                                         # 노드를 tree에 하나씩 추가할 때
        a = n + 1                                                   # a에 추가한 노드의 인덱스를 저장하고
        while a:                                                    # a가 0이 될때까지 반복해서
            if tree[a] < tree[a // 2]:                              # 부모노드보다 자식노드가 작다면
                tree[a], tree[a // 2] = tree[a // 2], tree[a]       # 두 수를 바꾼다
            a //= 2                                                 # 부모 노드로 올라가 위와 같은 과정을 반복한다

    ans = 0                                                         # 정답을 저장할 변수를 생성하고
    while 1:                                                        # break까지 반복할 때
        if N//2 == 1:                                               # N//2가 1인 root에 도달하면
            N = N // 2                                              # N을 N//2 값으로 저장하고
            ans += tree[N]                                          # ans에 tree[N]을 더한 뒤
            break                                                   # 반복문 종료
        else:                                                       # N//2가 root에 도달하지 못했다면
            N = N // 2                                              # N을 N//2 값으로 저장하고
            ans += tree[N]                                          # ans에 tree[N]을 더한다

    print(f'#{t+1}', ans)
