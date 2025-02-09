# AB-3_BOJ16428

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 두 수를 input 받고
ans = A%B                           # 나머지를 계산한 후
if ans < 0:                         # 나머지가 음수라면
    print(A//B+1)                   # 몫을 1 추가해서 출력하고
    print(ans-B)                    # 나머지를 B만큼 뺀 후 출력한다
else:                               # 나머지가 음수가 아니라면
    print(A//B)                     # 몫을 출력하고
    print(ans)                      # 나머지를 출력한다