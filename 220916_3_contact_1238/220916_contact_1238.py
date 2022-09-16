# contact_1238

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10                                              # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    L, S = map(int, input().split())                # L = 순서쌍의 길이 / S = 출발점
    N = [[] for _ in range(101)]                    # N = 전화를 걸 사람을 저장할 빈 리스트
    arr = list(map(int, input().split()))           # 순서쌍을 arr에 저장한다

    a = 0                                           # 인덱스로 사용할 변수 a를 생성하고
    while a <= L-1:                                 # a가 순서쌍만큼 도달할 때까지 반복
        N[arr[a]].append(arr[a+1])                  # 전화거는사람을 인덱스로 전화 받는사람을 요소로 리스트 N에 저장한다
        a += 2                                      # 인덱스를 2칸 넘어간다

    q = []                                          # 시작점부터 순서대로 전화할 q를 생성
    ans = []                                        # 전화 기록을 남길 ans 생성

    for a in N[S]:                                  # 시작점이 전화를 걸기 시작할 때
        q.append([a, 1])                            # 받는 사람을 q에 [받는사람, 걸린시간] 순서로 저장하고
        ans.append([1, a])                          # 받은 기록을 ans에 [걸린시간, 받은사람] 순서로 저장한 후
    N[S] = []                                       # 전화를 건 사람의 기록은 삭제 한다

    while q:                                        # q가 비어 비상 연락망의 끝까지 반복할 때
        A = q.pop(0)                                # q에서 전화 거는사람을 꺼내
        for b in N[A[0]]:                           # 전화를 걸기 시작해서
            for c in ans:                           # 받은 기록을 살펴봐서
                if c[1] == b:                       # 받은 기록이 있다면 전화를 취소하고
                    break
            else:                                   # 받은 기록이 없다면
                q.append([b, A[1] + 1])             # 받는 사람을 q에 [받는사람, 걸린시간] 순서로 저장하고
                ans.append([A[1] + 1, b])           # 받은 기록을 ans에 [걸린시간, 받은사람] 순서로 저장한다
        else:                                       # 모든 연락을 돌린 후
            N[A[0]] = []                            # 전화를 건 사람의 기록은 삭제 한다

    print(f'#{t+1}', max(ans)[1])                   # 가장 마지막에 받은 사람중 가장 숫자가 큰사람을 출력한다









