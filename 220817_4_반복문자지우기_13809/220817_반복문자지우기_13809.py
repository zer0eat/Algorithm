# 반복문자지우기_13809

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                # 테스트 케이스
for t in range(T):
    N = list(input())           # 문자를 지울 문자열

    G = len(N)                  # 문자열의 길이를 G에 저장
    n = 0                       # 문자열을 반복할 때 인덱스
    k = 0                       # 문자열에서 지운 문자의 수
    while n + k < G - 1:        # 문자열을 반복 맨뒤에서 한칸 앞자리 까지
        if N[n] == N[n+1]:      # 문자열이 다음 문자열과 같을 때
            del N[n+1]          # 다음문자열과
            del N[n]            # 현재문자열을 리스트에서 삭제
            k += 2              # 지운만큼 k에 추가
            n = 0               # 문자의 맨 앞열로 돌아감
        elif N[n] != N[n+1]:    # 문자열이 다음 문자열과 다를 때
            n += 1              # 다음문자열로 갈 수 있도록 인덱스 이동

    print(f'#{t+1}', len(N))