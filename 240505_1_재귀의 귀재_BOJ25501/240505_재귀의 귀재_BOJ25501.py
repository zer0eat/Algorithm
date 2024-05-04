# 재귀의 귀재_BOJ25501

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def recursion(s, l, r):
    global cnt                          # cnt를 global 변수로 선언하고
    cnt += 1                            # recursion의 시행 횟수를 추가한다
    if l >= r:                          # 왼쪽문자가 오른쪽 문자와 같거나 더 뒤에 있다면
        return 1                        # 1을 리턴하고
    elif s[l] != s[r]:                  # 왼쪽문자와 오른쪽 문자가 다르다면
        return 0                        # 0을 리턴하고
    else:                               # 왼쪽문자가 오른쪽 문자보다 앞에 있지만 같은 경우
        return recursion(s, l+1, r-1)   # 다음 문자를 팰린드롬인지 확인한다

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)    # 맨 앞글자와 맨 뒤글자가 팰린드롬인지 확인한다

T = int(input())                        # 테스트케이스를 input 받고
for t in range(T):                      # 테스트케이스를 반복해서
    word = input().strip()              # 단어를 input 받은 후
    cnt = 0                             # recursion 함수 시행 횟수를 저장할 변수를 생성하고
    print(isPalindrome(word), cnt)      # 팰린드롬여부와 recursion함수 시행 횟수를 출력한다