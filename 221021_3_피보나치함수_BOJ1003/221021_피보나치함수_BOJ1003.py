# 피보나치함수_BOJ1003

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def fiboancci(N):                       # 피보나치 함수를 구해서
    ans = [[1, 0], [0, 1]]              # 0과 1일 때 0과 1의 개수를 담을 리스트를 미리 넣어둔 리스트를 생성한다
    for i in range(2, N+1):             # 2부터 N까지 반복할 때
        ans.append([ans[i - 1][0] + ans[i - 2][0], ans[i - 1][1] + ans[i - 2][1]])  # N번째는 [N-1의 0의 숫자 + N-2의 0의 숫자, N-1의 1의 숫자 + N-2의 1의 숫자]
    return ans                          # ans를 return 한다

# input 받기
T = int(sys.stdin.readline())           # 테스트 케이스를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    N = int(sys.stdin.readline())       # 구하려는 피보나치 수열의 순번을 input받고

    print(*fiboancci(N)[N])             # 피보나치 수열을 구할 때 나오는 0과 1의 숫자를 출력한다