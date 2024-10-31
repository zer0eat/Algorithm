# 스키테일 암호_BOJ23080

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K = int(input())                    # 막대의 두께를 input 받고
ribbon = input().strip()            # 리본의 문자를 input 받는다
ans = ''                            # 정답을 저장할 변수를 생성하고
for a in range(0, len(ribbon), K):  # 막대의 두께만큼 반복해서
    ans += ribbon[a]                # 암호문을 변수에 더해준 후
print(ans)                          # 암호문을 출력한다