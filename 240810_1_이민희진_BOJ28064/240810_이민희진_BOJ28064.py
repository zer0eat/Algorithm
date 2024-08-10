# 이민희진_BOJ28064

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                                                 # 정답을 저장할 변수를 생성하고
N = int(input())                                        # 사람의 수를 input 받고
name = list(input().strip() for _ in range(N))          # 이름을 리스트로 저장한다
for n in range(N):                                      # 사람의 수를 반복하고
    for m in range(n+1, N):                             # n번 다음사람부터 반복해서
        if len(name[n]) < len(name[m]):                 # 두 사람 중 n번의 이름이 더짧다면
            A, B = name[n], name[m]                     # A에 짧은사람 이름을 저장하고 B에 긴사람 이름을 저장한다
        else:                                           # 두 사람 중 n번의 이름이 길다면
            B, A = name[n], name[m]                     # A에 긴사람 이름을 저장하고 B에 짧은사람 이름을 저장한다
        for k in range(len(A), -1, -1):                 # 짧은 이름의 길이를 역으로 반복해서
            if B[:k] == A[-k:] or B[-k:] == A[:k]:      # 앞부분이나 뒷부분이 겹친다면
                ans += 1                                # 정답에 1을 출력하고
                break                                   # for문을 break한다
print(ans)                                              # 이름이 겹치는 쌍을 출력한다