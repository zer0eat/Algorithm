# 욱제는 도박쟁이야!!_BOJ14655

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 동전의 수를 input 받고
r1 = list(map(int, input().split()))    # 1라운드 동전을 리스트로 input 받고
r2 = list(map(int, input().split()))    # 2라운드 동전을 리스트로 input 받는다
ans = 0                                 # 정답을 저장할 변수를 생성하고
for n in range(N):                      # 동전의 수를 반복해서
    ans += abs(r1[n]) + abs(r2[n])      # 동전의 절댓값을 변수에 더해준다
print(ans)                              # 욱제가 이번 게임에서 획득할 점수를 출력한다