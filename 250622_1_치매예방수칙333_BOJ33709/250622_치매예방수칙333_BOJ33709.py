# 치매예방수칙333_BOJ33709

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 슬로건의 길이를 inputqkerh
ans = 0                         # 정답을 저장할 변수를 생성한다
S = input().strip()             # 슬로건을 input받고
tmp = ''                        # 숫자를 저장할 변수를 생성한다
for s in S:                     # 슬로건을 반복해서
    if s in ['.','|',':','#']:  # 특수기호가 나왔다면
        ans += int(tmp)         # 여태까지 숫자를 정답에 저장하고
        tmp = ''                # 초기화 한다
    else:                       # 숫자가 나왔다면
        tmp += s                # 숫자를 저장할 변수에 더해준다
else:                           # 슬로건이 끝났다면
    ans += int(tmp)             # 숫자를 더해주고
print(ans)                      # 정답을 출력한다