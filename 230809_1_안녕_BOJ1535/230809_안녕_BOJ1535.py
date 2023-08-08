# 안녕_BOJ1535

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                            # 사람의 수를 input 받고
hi = [list(map(int, input().split())) for _ in range(2)]                    # 첫째 행에 인사할 때 잃는 체력 / 둘째 행에 인사할 때 얻는 행복을 행렬 형태로 input 받는다
hi[0] = [0] + hi[0]                                                         # 인덱스와 사람의 번호를 맞춰주기 위해 체력 정보 앞에 0 원소를 추가한다
hi[1] = [0] + hi[1]                                                         # 인덱스와 사람의 번호를 맞춰주기 위해 행복 정보 앞에 0 원소를 추가한다
dp = [[0] * 101 for _ in range(N+1)]                                        # 체력에 따른 행복을 저장하기 위해 0부터 100까지 체력을 담은 리스트를 사람의 수 만큼 리스트에 담아 생성한다
for i in range(1, N+1):                                                     # 사람의 수를 1부터 N까지 반복해서
    for j in range(1, 101):                                                 # 해당 사람의 체력을 1부터 100까지 반복한다
        if hi[0][i] <= j:                                                   # i번째 사람과 인사할 때 드는 체력소모가 j보다 같거나 작을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hi[0][i]] + hi[1][i])      # i번째 사람의 j만큼의 체력이 있을 때 i와는 인사하지 않았을 때 행복과 i와 인사하고 그 만큼 체력을 소모했을 때 행복 중 행복이 더 큰 값을 저장한다
        else:                                                               # 만약 i번째 사람과 인사할 때 드는 체력소모가 j보다 클 때
            dp[i][j] = dp[i-1][j]                                           # i번째 사람의 j만큼의 체력이 있을 때 i와는 인사하지 않았을 때 행복을 저장한다
print(dp[N][99])                                                            # 세준이가 얻을 수 있는 최대 기쁨을 출력한다