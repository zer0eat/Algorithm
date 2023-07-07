# 카드문자열_BOJ13417

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스
for t in range(T):                      # 테스트 케이스를 반복해서
    N = int(input())                    # 알파벳 카드의 수를 input 받는다
    lst = list(input().split())         # 알파벳 카드를 리스트로 input 받는다
    ans = lst[0]                        # 알파벳 카드의 첫 카드를 ans에 저장하고
    for n in range(1, N):               # 그 다음 카드부터 반복해서
        if ord(ans[0]) < ord(lst[n]):   # ans에 저장된 맨 앞 카드보다 n번째 카드가 사전순으로 뒤에 있다면
            ans += lst[n]               # ans 뒤에 붙여주고
        else:                           # ans에 저장된 맨 앞 카드보다 n번째 카드가 사전순으로 같거나 앞에 있다면
            ans = lst[n] + ans          # ans 앞에 붙여준다
    print(ans)                          # 모든 알파벳 카드를 반복했다면 ans를 출력한다