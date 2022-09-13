# 노드의합_14075

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                            # 테스트 케이스
for t in range(T):                                          # 테스트 케이스를 반복할 때
    N, M, L = map(int, input().split())                     # N 전체 노드의 숫자 / M 정보를 제공할 노드의 숫자 / L 알고 싶은 노드 번호
    word = [''] * (N + 1)                                   # 노드의 값을 저장할 리스트를 만든다

    for m in range(M):                                      # M번 반복할 때
        i, X = map(int, input().split())                    # i 노드의 인덱스 / X 노드의 값
        word[i] = X                                         # word에 인덱스에 맞게 X 값을 저장

    for b in range(len(word)-1, 0, -1):                     # word를 뒤에서부터 살펴볼 때
        if word[b] == '':                                   # 비어 있는 칸이 나오면
            try:                                            # 양쪽 자식이 다 있으면
                word[b] = word[2 * b] + word[2 * b + 1]     # 양쪽 자식을 더한 값을 부모노드의 값에 저장하고
            except:                                         # 한쪽 자식만 있다면
                word[b] = word[2 * b]                       # 왼쪽 자식의 값만 부모노드의 값에 저장한다
        else:                                               # 값이 이미 있다면 패스
            pass
    else:                                                   # 반복을 마치면 L자리의 노드 값을 출력한다
        print(f'#{t+1}', word[L])