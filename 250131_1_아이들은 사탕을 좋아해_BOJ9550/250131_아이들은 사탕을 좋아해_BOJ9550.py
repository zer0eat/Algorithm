# 아이들은 사탕을 좋아해_BOJ9550

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N, K = map(int, input().split())        # 사탕의 수와 먹어야하는 수를 input 받고
    candy = list(map(int, input().split())) # 종류별 사탕의 수를 input 받고
    ans = 0                                 # 정답을 저장할 변수를 생성한다
    for c in candy:                         # 사탕의 수를 반복해서
        ans += c//K                         # 행복한 사람을 변수에 더해주고
    print(ans)                              # 행복한 사람의 수를 출력한다