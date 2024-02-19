# 캔 주기_BOJ25602

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                                # N 캔의 수 / K 고양이에게 밥을 줄 날을 input 받고
can = list(map(int, input().split()))                           # 가지고 있는 캔의 수를 리스트로 input 받는다
rang = [list(map(int, input().split())) for _ in range(K)]      # 랑이의 만족도를 리스트로 input 받고
merry = [list(map(int, input().split())) for _ in range(K)]     # 메리의 만족도를 리스트로 input 받고
ans = 0                                                         # 정답을 저장할 변수를 생성한다

def recur(dep, tmp):
    global ans                                                  # ans를 global 변수로 선언하고
    if dep == K:                                                # 모든날 만족도가 더해졌다면
        ans = max(ans, tmp)                                     # ans와 tmp 중 큰 만족도를 ans에 저장하고
        return                                                  # return한다
    for i in range(N):                                          # 캔의 수를 반복해서
        if can[i]:                                              # i번째 캔이 남아 있다면
            can[i] -= 1                                         # i번째 캔을 1개 제거하고
            tmp += rang[dep][i]                                 # dep일의 i캔을 먹었을 때 랑이의 만족도를 더하고
            for j in range(N):                                  # 캔의 수를 반복해서
                if can[j]:                                      # j번째 캔이 남아 있다면
                    can[j] -= 1                                 # j번째 캔을 1개 제거하고
                    tmp += merry[dep][j]                        # dep일의 j캔을 먹었을 때 메리의 만족도를 더하고
                    recur(dep+1, tmp)                           # 깊이 dep+1부터 만족도를 탐색한다
                    tmp -= merry[dep][j]                        # dep일의 j캔을 먹었을 때 메리의 만족도를 빼주고
                    can[j] += 1                                 # j번째 캔을 1개 복구하고
            tmp -= rang[dep][i]                                 # dep일의 i캔을 먹었을 때 랑이의 만족도를 뺴주고
            can[i] += 1                                         # i번째 캔을 1개 복구한다

recur(0,0)                                                      # 깊이 0 부터 만족도를 탐색한다
print(ans)                                                      # 랑이와 메리의 만족도의 합의 최댓값을 출력한다