# 회문_BOJ14561

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input 받고

def solution(n, q):
    lst = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}  # 11진수 이상일 때 변환되는 값을 딕셔너리로 생성한다
    rev_base = ''                       # 변환된 값을 저장할 변수를 생성하고
    while n > 0:                        # 양수라면
        n, mod = divmod(n, q)           # n을 q로 나눈 몫과 나머지를 구해서
        if mod > 9:                     # 나머지가 9보다 크면
            mod = lst[mod]              # 대응되는 값으로 나머지를 변경하고
        rev_base += str(mod)            # 나머지를 저장한다
    return rev_base[::-1] , rev_base    # q진수로 변환된 값과 뒤집어진 값을 리턴한다

for t in range(T):                      # 테스트케이스를 반복해서
    A, n = map(int, input().split())    # 10진수와 변환할 진수를 input 받고
    ans, rev_ans = solution(A, n)       # A를 n진수로 변환한 값과 뒤집어진 값을 저장한다
    if ans == rev_ans:                  # 두 값이 팰린드롬이라면
        print(1)                        # 1을 출력하고
    else:                               # 그렇지 않으면
        print(0)                        # 0을 출력한다