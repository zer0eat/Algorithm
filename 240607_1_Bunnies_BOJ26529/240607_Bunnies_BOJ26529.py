# Bunnies_BOJ26529

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = [1]*46                        # 정답을 저장할 리스트를 생성하고
for i in range(2, 46):              # 2부터 45번째 까지 반복해서
    ans[i] = ans[i-1] + ans[i-2]    # 피보나치 수열을 구해서 저장한다
N = int(input())                    # 테스트케이스를 input 받고
for n in range(N):                  # 테스트케이스를 반복해서
    X = int(input())                # 개월 수를 input 받고
    print(ans[X])                   # x개월 후 예상되는 토끼 수를 출력한다