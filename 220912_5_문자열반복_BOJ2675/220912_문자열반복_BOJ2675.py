# 문자열반복_BOJ2675

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())            # 테스트케이스
for t in range(T):          # 테스트 케이스 반복
    R, S = input().split()  # R은 반복할 숫자 S는 반복할 문자열
    R = int(R)              # 문자열로 받은 R을 int로 변환한 뒤
    ans = ''                # 정답을 넣을 빈 문자열을 만들고
    for s in S:             # 문자열을 반복하여
        ans += s*R          # R만큼의 문자를 ans에 더한 후
    else:                   # 반복이 끝나면 출력한다
        print(ans)

