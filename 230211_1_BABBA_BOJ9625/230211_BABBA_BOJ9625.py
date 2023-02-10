# BABBA_BOJ9625

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
K = int(sys.stdin.readline())   # 버튼을 누를 숫자를 input 받고

ans = [1, 0]                    # ans에 A와 B의 개수를 저장한다
for _ in range(K):              # K번 반복할때
    A = ans[0]                  # A에 개수를 A에 저장하고
    B = ans[1]                  # B의 개수를 B에 저장한다
    ans[0] = ans[0] - A + B     # ans의 A가 저장되는 자리에는 A를 빼고 B를 더하고
    ans[1] += A                 # ans의 B가 저장되는 자리에는 A를 더한다
else:                           # K번 반복을 마쳤다면
    print(*ans)                 # ans를 출력한다