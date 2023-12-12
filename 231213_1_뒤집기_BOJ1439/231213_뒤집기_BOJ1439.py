# 뒤집기_BOJ1439

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip()         # 문자열을 input 받고
N = len(S)                  # 문자열의 길이를 변수에 저장한다
ans = 0                     # 뒤집기 행동 횟수를 저장할 변수를 생성하고
start = S[0]                # 시작 문자열을 저장한다
flag = True                 # 뒤집기를 해야하는지 표시할 변수를 생성하고
for i in range(N):          # 문자열을 반복해서
    if S[i] == start:       # 첫번째 문자열과 같을 때
        if flag == False:   # flag가 False인 경우
            flag = True     # flag를 True로 바꿔서 이후 나오는 문자열이 다르다면 뒤집어야한다는 표시 해준다
    else:                   # 첫번째 문자열과 다들 때
        if flag:            # flag가 True인 경우
            ans += 1        # 뒤집을 횟수를 1 추가하고
            flag = False    # flag를 False로 바꿔서 이후 나오는 문자열이 첫번째 문자열과 다르더라도 뒤집기 횟수를 추가하지 않도록 표시 해준다
print(ans)                  # 뒤집기 최소횟수를 출력한다