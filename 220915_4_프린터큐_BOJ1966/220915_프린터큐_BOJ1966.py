# 프린터큐_BOJ1966

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스를 반복할 때
    N, M = map(int, input().split())        # N은 출력물의 개수 / M 몇번째로 출력되는지 알고 싶은 출력물의 인덱스
    pQ = list(map(int, input().split()))    # 출력물을 리스트 형태로 받음
    for p in range(len(pQ)):                # 출력물을 돌아가면서
        pQ[p] = [pQ[p], p]                  # 리스트 형태로 중요도와 인덱스를 붙여줌
    printQ = []                             # 출력 순서대로 저장할 빈 리스트 생성
    while pQ:                               # 프린트가 완료될 때까지 반복할 때
        q = pQ.pop(0)                       # 맨앞에서 출력물을 빼서 q로 저장한 후
        if len(pQ) == 0:                    # 더이상 출력할 문서가 없을 때
            printQ.append(q)                # printQ에 append 해서 출력
        elif q[0] >= max(pQ)[0]:            # 중요도가 남은 출력물중 가장 높을 때
            printQ.append(q)                # printQ에 append 해서 출력
        else:                               # 더 중요한 출력물이 남았다면
            pQ.append(q)                    # pQ에 append 해서 뒤로 보냄

    for a in range(len(printQ)):            # 출력물을 순서대로 확인할 때
        if printQ[a][1] == M:               # M을 인덱스로 갖고 있었던 출력물이 나오면
            print(a+1)                      # 출력된 순서를 프린트한다
            break