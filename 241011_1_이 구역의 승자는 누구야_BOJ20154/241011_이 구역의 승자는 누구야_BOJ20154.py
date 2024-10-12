# 이 구역의 승자는 누구야_BOJ20154

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
alphabet = {
    'A' : 3,
    'B' : 2,
    'C' : 1,
    'D' : 2,
    'E' : 3,
    'F' : 3,
    'G' : 3,
    'H' : 3,
    'I' : 1,
    'J' : 1,
    'K' : 3,
    'L' : 1,
    'M' : 3,
    'N' : 3,
    'O' : 1,
    'P' : 2,
    'Q' : 2,
    'R' : 2,
    'S' : 1,
    'T' : 2,
    'U' : 1,
    'V' : 1,
    'W' : 2,
    'X' : 2,
    'Y' : 2,
    'Z' : 1
}                                           # 알파벳 획수 딕셔너리를 생성하고
S = list(input().strip())                   # 문자를 리스트로 input 받고
K = len(S)                                  # 문자의 길이를 저장한다
for s in range(K):                          # 문자의 길이를 반복해서
    S[s] = alphabet[S[s]]                   # 문자 별 획수로 변환한다
while K > 1:                                # 한 숫자만 남을 때까지 반복해서
    tmp = []                                # 리스트를 생성하고
    if K % 2:                               # 남은 문자의 수가 홀수라면
        for k in range(0,K-1,2):            # 홀수번째 수를 반복해서
            tmp.append((S[k] + S[k+1])%10)  # 홀수와 짝수번째 수를 더해서 일의 자리만 tmp에 더해준다
        else:                               # 마지막 문자 전까지 반복을 마친 후
            tmp.append(S[-1])               # 마지막 수를 tmp에 더해준다
    else:                                   # 남은 문자의 수가 짝수라면
        for k in range(0,K,2):              # 홀수번째 수를 반복해서
            tmp.append((S[k] + S[k+1])%10)  # 홀수와 짝수번째 수를 더해서 일의 자리만 tmp에 더해준다
    S = tmp                                 # S를 tmp로 저장하고
    K = len(S)                              # S의 길이를 K에 저장한다
if S[-1] % 2:                               # 마지막 남은 숫자가 홀수라면
    print("I'm a winner!")                  # I'm a winner!을 출력한다
else:                                       # 마지막 남은 숫자가 짝수라면
    print("You're the winner?")             # You're the winner?을 출력한다