# 파스칼 삼각형_2005

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):
    N = int(input())                        # 파스칼 삼각형의 길이
    memo = []                               # 파스칼 삼각형을 저장할 리스트
    print(f'#{t + 1}')                      # 테스트 케이스 번호 출력
    # 파스칼 삼각형의 길이로 반복문을 돌려서
    for n in range(N):
        pascal_triangle = ([1] * (n+1))     # 길이에 맞는 길이를 생성
        for m in range(n+1):                # 삼각형의 한 변을 반복문을 돌려서
            if m == 0 or m == n:            # 처음과 끝 자리는 1
                pass
            else:                           # 처음과 끝 자리가 아니면
                                            # 바로 윗줄에서 나와 같은 인덱스의 요소, 하나 전의 요소를 더한 값을 저장한다
                pascal_triangle[m] = memo[n-1][m-1] + memo[n-1][m]
        else:
            memo.append(pascal_triangle)    # memo 리스트에 각각의 변을 저장하고
            print(*pascal_triangle)         # 해당 변을 출력한다.
