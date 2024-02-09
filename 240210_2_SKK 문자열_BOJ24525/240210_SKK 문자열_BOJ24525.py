# SKK 문자열_BOJ24525

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip()                                 # 문자열의 길이를 input 받고
dp = [0] * (len(S)+1)                               # S와 K의 수를 저장할 리스트를생성한다
for s in range(len(S)):                             # 문자열의 길이를 반복해서
    if S[s] == 'S':                                 # S가 나오면
        dp[s+1] = dp[s] + 2                         # 이전 원소에서 2를 더해주고
    elif S[s] == 'K':                               # K가 나오면
        dp[s+1] = dp[s] - 1                         # 이전 원소에서 1을 빼준다
    else:                                           # 다른 문자열은
        dp[s+1] = dp[s]                             # 이전 원소와 같은 값을 저장한다
ans = -1                                            # 정답을 저장할 변수를 생성하고
dic = dict()                                        # 길이를 확인할 딕셔너리를 생성하고
flag = -1                                           # 이전까지 SK의 합을 저장할 변수를 생성하다
for i in range(len(dp)):                            # dp를 반복해서
    if dp[i] != flag and dic.get(dp[i]) == None:    # flag와 다르고 딕셔너리에 해당 원소가 없다면
        flag = dp[i]                                # flag를 원소로 저장하고
        dic[dp[i]] = i                              # dp[i]를 key로 인덱스를 value로 원소를 생성한다
    elif dp[i] != flag and dic.get(dp[i]) != None:  # flag와 다르고 딕셔너리에 해당 원소가 있다면
        ans = max(ans, i - dic[dp[i]])              # 정답을 최대 길이로 저장하고
        flag = ''                                   # flag를 삭제한다
print(ans)                                          # 문자열 중 길이가 가장 긴 SKK 문자열의 길이를 출력한다